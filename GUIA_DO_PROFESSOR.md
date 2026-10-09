# Guia do professor — Gitópolis 1.0

## Objetivo

Fixar noções de histórico de alterações, repositórios, staging, commits, branches, merge, sincronização com repositório remoto e colaboração por pull requests. O jogo oferece um terminal simulado; a aprendizagem precisa ser consolidada também num repositório Git real.

**Público sugerido:** turmas de desenvolvimento de sistemas e introdução à programação.

**Organização sugerida:** uma aula de apresentação e exploração do jogo; outra de prática guiada no VS Code; uma terceira para o desafio em grupos.

## Gabarito das 20 missões

Os comandos abaixo são exemplos aceitos. O estudante pode escolher outro nome de autoria, e-mail fictício, mensagem descritiva de commit ou URL sintaticamente válida do GitHub em algumas etapas. Links de repositórios são ilustrativos e não precisam existir.

| Nº | Missão | Solução esperada |
|---|---|---|
| 01 | A central de ferramentas | `git --version` |
| 02 | Quem está programando? | `git config --global user.name "Ana Silva"` |
| 03 | Assinatura do commit | `git config --global user.email "ana@exemplo.com"` |
| 04 | Fundação do repositório | `git init -b main` |
| 05 | Detetives do código | `git status` |
| 06 | Antes e depois | `git diff` |
| 07 | Preparar a entrega | `git add index.html` → `git diff --staged` |
| 08 | Primeiro ponto de controle | `git commit -m "Cria pagina inicial"` → `git log --oneline` |
| 09 | Uma rua só para o menu | `git switch -c feature/menu` → `git branch` |
| 10 | Revisão no branch | `git diff` |
| 11 | Entrega isolada | `git add menu.js` → `git commit -m "Adiciona menu"` |
| 12 | Avenida da integração | `git switch main` → `git merge feature/menu` |
| 13 | Conexão com a nuvem | `git remote add origin https://github.com/equipe/cidade-digital.git` |
| 14 | Inspecionar conexão | `git remote -v` |
| 15 | Publicar o projeto | `git push -u origin main` |
| 16 | Atualização da equipe | `git fetch origin` → `git pull origin main` |
| 17 | Novo projeto da escola | `git clone https://github.com/equipe/portal-escola.git` |
| 18 | Tela de contato em equipe | `git switch -c feature/contato` |
| 19 | Enviar a colaboração | `git add contato.html` → `git commit -m "Cria pagina contato"` → `git push -u origin feature/contato` |
| 20 | A revisão final | Na interface simulada: criar pull request → revisar → merge |

### Pontos de atenção didáticos

- `git` é o sistema de versionamento; o **GitHub** é um serviço que hospeda repositórios e oferece ferramentas de colaboração.
- `git add` prepara conteúdo, `git commit` cria um registro **local** e `git push` publica commits no remoto.
- `git diff` e `git diff --staged` não exibem a mesma comparação.
- `git switch -c` cria e seleciona um branch; `git merge feature/menu` integra o branch indicado **ao branch atual**.
- `git fetch` atualiza referências remotas sem mesclar automaticamente; `git pull` também integra alterações ao branch atual, conforme a configuração.
- Para pull requests, normalmente há revisão por outro integrante da equipe antes da integração. Abrir um PR é um fluxo da interface ou API do GitHub, não um comando Git básico.
- Configurações `user.name` e `user.email` determinam a autoria dos commits; não são credenciais de login.
- Em projetos reais, comandos podem falhar por conflitos, permissões, autenticação ou ausência de commits. O jogo simplifica esses casos.

## Proposta complementar: Gitópolis real (equipes de três)

**Situação:** a prefeitura fictícia quer um pequeno portal com páginas Inicial, Serviços e Contato. Três estudantes desenvolvem o portal simultaneamente.

1. Um integrante cria um repositório no GitHub, inicializa o projeto e adiciona os colegas como colaboradores, quando necessário.
2. Cada aluno clona o repositório e cria **seu próprio branch**, por exemplo `feature/inicial`, `feature/servicos` e `feature/contato`.
3. Cada aluno cria ou modifica arquivos HTML/CSS/JS correspondentes à sua página, consulta `git status`/`git diff`, registra ao menos dois commits com mensagens descritivas e publica o branch.
4. Cada estudante abre um pull request destinado a `main`. Os colegas revisam as alterações e registram sugestões quando necessário.
5. Após a integração dos pull requests, todos executam `git pull origin main`, conferem o histórico e testam o portal completo.

**Evidências a entregar:** URL do repositório, nomes dos branches, links dos pull requests, histórico de commits e relatório individual do Gitópolis (HTML convertido em PDF, se solicitado).

**Rubrica opcional (10 pontos):** versionamento correto e histórico (3,0); uso de branches e colaboração (2,0); pull requests/revisões (2,0); funcionamento do portal (2,0); organização das entregas (1,0).

## Sobre os resultados

O jogo acompanha 20 missões, progresso percentual, pontos (até 2.000), comandos incorretos e uso de dicas. O relatório é salvo no dispositivo do estudante, sem armazenamento central. O resultado não substitui a verificação da atividade prática em um repositório real.

## Referências oficiais

- Git — manual de comandos: https://git-scm.com/docs
- Git — `git status`: https://git-scm.com/docs/git-status
- Git — `git add`: https://git-scm.com/docs/git-add
- GitHub — fluxo de colaboração: https://docs.github.com/pt/pull-requests/concepts/writing-code-for-a-project
- GitHub — exercício introdutório: https://docs.github.com/en/get-started/using-github/hello-world
