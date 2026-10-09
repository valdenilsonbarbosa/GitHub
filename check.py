from playwright.sync_api import sync_playwright
from pathlib import Path
import json
p='http://127.0.0.1:8765/index.html'
import subprocess, time
server=subprocess.Popen(['python','-m','http.server','8765','--bind','127.0.0.1'],cwd='/mnt/data/gitopolis',stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
time.sleep(.8)
with sync_playwright() as play:
 b=play.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu'])
 page=b.new_page(viewport={'width':1440,'height':900},device_scale_factor=1,accept_downloads=True)
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto(p,wait_until='load',timeout=25000)
 page.wait_for_timeout(800)
 print('TITLE:',page.title())
 print('Initial:',page.locator('#hudCount').inner_text(), 'Welcome:',page.locator('#welcomeOverlay').get_attribute('class'))
 page.screenshot(path='/mnt/data/gitopolis/preview_city.png',full_page=False)
 page.locator('#startButton').click()
 page.locator('#playNext').click()
 print('MISSION OPEN:',page.locator('#missionTitle').inner_text())
 page.screenshot(path='/mnt/data/gitopolis/preview_mission.png',full_page=False)
 # Execute first and confirm automatic city return
 page.locator('#terminalInput').fill('git --version')
 page.locator('#terminalForm button').click()
 print('AFTER FIRST:',page.locator('#hudCount').inner_text(), 'FEEDBACK:',page.locator('#feedback').inner_text()[:70])
 page.wait_for_timeout(4700)
 print('RETURN AFTER 4.5s:',page.locator('#missionOverlay').get_attribute('class'))
 for k, cmds in enumerate([
  ['git config --global user.name "Ana Silva"'],
  ['git config --global user.email "ana@exemplo.com"'],
  ['git init -b main'],
  ['git status'],['git diff'],['git add index.html'],['git commit -m "Cria pagina inicial"'],
  ['git switch -c feature/menu'],['git diff'],['git add menu.js','git commit -m "Adiciona menu"'],
  ['git switch main','git merge feature/menu'],
  ['git remote add origin https://github.com/equipe/cidade-digital.git'],
  ['git remote -v'],['git push -u origin main'],['git fetch origin','git pull origin main'],
  ['git clone https://github.com/equipe/portal-escola.git'],
  ['git switch -c feature/contato'],
  ['git add contato.html','git commit -m "Cria pagina contato"','git push -u origin feature/contato'],
 ]):
  idx=k+1
  page.locator('#missionOverlay').evaluate('el => el.classList.remove("visible")') if page.locator('#missionOverlay').get_attribute('class').endswith('visible') else None
  # removing visible manually does not clear auto timer: openMission clears
  page.locator('#playNext').click(timeout=10000)
  for c in cmds:
   page.locator('#terminalInput').fill(c)
   page.locator('#runCommand').click()
  if page.locator('#hudCount').inner_text().strip()!=f'{idx+1} / 20':
   print('FAIL step:',idx+1,'hud=',page.locator('#hudCount').inner_text(), 'screen=',page.locator('#terminalScreen').inner_text()[-180:]);break
 else:
  page.locator('#missionOverlay').evaluate('el => el.classList.remove("visible")')
  page.locator('#playNext').click()
  for i in range(3):
   page.locator(f'#githubActions button[data-pr="{i}"]').click()
  print('MISSION 20:',page.locator('#hudCount').inner_text(),page.locator('#feedback').inner_text()[:110]);
 page.locator('#missionOverlay').evaluate('el => el.classList.remove("visible")')
 page.locator('#reportButton').click()
 print('REPORT:',page.locator('#reportPct').inner_text())
 with page.expect_download() as down:
  page.locator('#downloadReport').click()
 dl=down.value;print('DOWNLOAD:',dl.suggested_filename)
 page.screenshot(path='/mnt/data/gitopolis/preview_report.png',full_page=False)
 print('JS ERRORS:',errors[:6], 'Count:',len(errors))
 b.close()
server.terminate()
