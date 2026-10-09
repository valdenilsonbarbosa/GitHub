from playwright.sync_api import sync_playwright
from pathlib import Path
html=Path('/mnt/data/gitopolis/index.html').read_text()
missions=[
 ['git --version'],['git config --global user.name "Ana Silva"'],['git config --global user.email "ana@exemplo.com"'],['git init -b main'],
 ['git status'],['git diff'],['git add index.html','git diff --staged'],['git commit -m "Cria pagina inicial"','git log --oneline'],
 ['git switch -c feature/menu','git branch'],['git diff'],['git add menu.js','git commit -m "Adiciona menu"'],
 ['git switch main','git merge feature/menu'],['git remote add origin https://github.com/equipe/cidade-digital.git'],
 ['git remote -v'],['git push -u origin main'],['git fetch origin','git pull origin main'],
 ['git clone https://github.com/equipe/portal-escola.git'],['git switch -c feature/contato'],
 ['git add contato.html','git commit -m "Cria pagina contato"','git push -u origin feature/contato'],
]
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu'])
 page=b.new_page(viewport={'width':1440,'height':900},accept_downloads=True)
 page_errors=[];page.on('pageerror',lambda e:page_errors.append(str(e)))
 page.set_content(html)
 page.locator('#startButton').click()
 for ix,cmds in enumerate(missions):
  page.locator('#playNext').click()
  for cmd in cmds:
   page.locator('#terminalInput').fill(cmd)
   page.locator('#runCommand').click()
  assert page.locator('#hudCount').inner_text()==f'{ix+1} / 20',f'Wrong progress at {ix+1}'
  page.locator('#goBack').click()
 page.locator('#playNext').click()
 for ix in range(3):
  page.locator(f'#githubActions button[data-pr="{ix}"]').click()
 assert page.locator('#hudCount').inner_text()=='20 / 20'
 page.locator('#goBack').click()
 page.locator('#reportButton').click()
 assert page.locator('#reportPct').inner_text()=='100%'
 with page.expect_download() as download_info:
  page.locator('#downloadReport').click()
 dl=download_info.value
 assert dl.suggested_filename=='gitopolis_relatorio.html'
 path='/mnt/data/gitopolis/test_report.html';dl.save_as(path)
 print('20/20 MISSIONS PASSED; Github PR workflow passed; report download:',dl.suggested_filename)
 print('Report size:',Path(path).stat().st_size,'bytes, 100% progress; JS page errors:',len(page_errors))
 if page_errors:print(page_errors)
 b.close()
