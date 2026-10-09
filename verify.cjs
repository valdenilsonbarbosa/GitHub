const fs=require('fs'),vm=require('vm');
let html=fs.readFileSync('/mnt/data/gitopolis/index.html','utf8');
let js=html.match(/<script>([\s\S]*)<\/script>/)[1];
let ls={};let nodes={};
function node(id){return nodes[id]||(nodes[id]={id,style:{},dataset:{},disabled:false,value:'',textContent:'',innerHTML:'',classList:{x:new Set(),add(c){this.x.add(c)},remove(c){this.x.delete(c)},contains(c){return this.x.has(c)},toggle(c,f){if(f===undefined? !this.x.has(c):f){this.x.add(c);return true}else{this.x.delete(c);return false}}},appendChild(){},focus(){},addEventListener(){},getBoundingClientRect(){return {width:1200,height:800}},querySelector(){return node('mockInput')},getContext(){return {}},setPointerCapture(){},scrollHeight:0});}
let ctx={console,window:{devicePixelRatio:1,addEventListener(){}},document:{body:{style:{}},getElementById:node,querySelectorAll:()=>[],createElement:()=>node('newElement'),addEventListener(){}},navigator:{},localStorage:{getItem:k=>ls[k]||null,setItem:(k,v)=>{ls[k]=v}},sessionStorage:{getItem:()=> '1'},ResizeObserver:class{observe(){}},requestAnimationFrame(){return 0},cancelAnimationFrame(){},setTimeout(){return 1},clearTimeout(){},performance:{now(){return 1}},confirm(){return true},Blob,URL,Date};vm.createContext(ctx);
try{vm.runInContext(js,ctx)}catch(e){console.error('Script initialization error',e);process.exit(1)}
function check(s){return vm.runInContext(s,ctx)}
const tests=[
['git --version'],['git config --global user.name "Ana Silva"'],['git config --global user.email "ana@exemplo.com"'],['git init -b main'],
['git status'],['git diff'],['git add index.html','git diff --staged'],['git commit -m "Cria pagina inicial"','git log --oneline'],
['git switch -c feature/menu','git branch'],['git diff'],['git add menu.js','git commit -m "Adiciona menu"'],
['git switch main','git merge feature/menu'],['git remote add origin https://github.com/equipe/cidade-digital.git'],
['git remote -v'],['git push -u origin main'],['git fetch origin','git pull origin main'],
['git clone https://github.com/equipe/portal-escola.git'],['git switch -c feature/contato'],
['git add contato.html','git commit -m "Cria pagina contato"','git push -u origin feature/contato']
];
let errors=[];
let first=check('firstPending()');if(first!==0)errors.push('First mission incorrect: '+first);
check('openMission(0)');check('execute("git global name.user")');
if(check('firstPending()')!==0 || check('mistakes[0]')!==1)errors.push('Invalid command not rejected correctly');
for(let i=0;i<tests.length;i++){
 try{check(`openMission(${i})`);for(let c of tests[i]){let quoted=JSON.stringify(c);check('execute('+quoted+')')};if(check('done.size')!==i+1)errors.push(`Mission ${i+1}: not complete, step=${check('stepIdx')}, feedback=${nodes.feedback.textContent}`);check('closeOverlay("missionOverlay")');}catch(e){errors.push('mission '+i+': '+e.stack);break}
}
try{check('openMission(19)');check('stepIdx++');check('stepIdx++');check('stepIdx++');check('finishMission()');if(check('done.size')!==20)errors.push('PR not complete');}catch(e){errors.push('PR: '+e.stack)}
console.log('Tested:',tests.length,'terminal missions + 1 GitHub PR mission');
console.log('Completed missions:',check('done.size'));
console.log('Score:',nodes.hudScore.textContent,'Progress:',nodes.hudCount.textContent);
console.log('Bad command mistakes:',check('mistakes[0]'));
console.log('Persistent saved state:',Object.keys(JSON.parse(ls['gitopolis-v1-progress']||'{}')).join(', '));
console.log('ERRORS:',errors.length);errors.forEach(e=>console.log(e));if(errors.length)process.exit(1);
