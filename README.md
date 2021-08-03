# Exercício Programa - Programação Orientada a Objeto

## Procedimento para utilização do repositório no Ubuntu
Esse template foi desenvolvido com intuito de facilitar a compilação e a correção do EP.

Lembre-se que seus veteranos continuam totalmente disponíveis para ajuda-los.

### 1. Use this template
Primeiramente aperte no botão verde "use this template" e crie esse repositório no seu github pessoal.

### 2. Git clone
No seu github pessoal, acesse o repositório criado e adquira o link dele em "Code" -> "HTTPS".

Por exemplo: https://github.com/User/TemplateOO.git

E no seu terminal, no diretório em que deseja armazena-lo rode:
```bash
git clone https://github.com/User/TemplateOO.git
```

### 3. Instruções para C++
#### Install CMake
Dentro do diretório criado rode:
```bash
chmod -x utils.sh install_cmake.sh
./install_cmake.sh
```

Com o cmake instalado você está pronto para desenvolver seu EP.

O esqueleto do seu código está na pasta src/drone.
#### Funções disponiveis 
Para compilar, rodar e testar seu código use as seguintes funções:

- Help: Lista as funções disponíveis
```bash
./utils.sh -h
```

- Analisa CMakeLists: Antes da compilação essa etapa é necessária. (Testes são desabilitados)
```bash
./utils.sh -c ./ build
```

- Build: Compila 
```bash
./utils.sh -b build
```
- Run: Roda o programa
```bash
./utils.sh -r
```
- Habilita os testes: Após habilitar os testes lembre de buildar novamente 
```bash
./utils.sh -C build
```

- Testa: Corrige seu EP
```bash
./utils.sh -t
```

- Testa (modo verborrágico): Corrige seu EP e te mostra com detalhes a verificação
```bash
./utils.sh -vt
```

- Build and Run: Compila e roda o código
```bash
./utils.sh --build -and-run
```

### 4. Instruções para Python
