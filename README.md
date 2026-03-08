# MIDI Project

Aplicação Python para reprodução e interação com MIDI, construída com arquitetura limpa e múltiplas opções de interface: CLI, aplicação web com Flask e interface desktop com Tkinter.

---

## Estrutura do Projeto

```
MIDI_project/
├── main.py
├── requirements.txt
├── test.py
└── src/
    ├── application/
    │   └── player_service.py        # Camada de aplicação / casos de uso
    ├── domain/
    │   ├── bpm.py                   # Lógica de BPM
    │   ├── music_theory.py          # Utilitários de teoria musical
    │   └── notes.py                 # Definição de notas
    └── infrastructure/
        ├── adapters/
        │   └── mido_adapter.py      # Adaptador MIDI usando mido
        └── ui/
            ├── cli/
            │   └── cli_app.py       # Interface de linha de comando
            ├── flask/
            │   ├── flask_app.py     # Aplicação web Flask
            │   ├── instance.py
            │   ├── controllers/
            │   │   └── player_controller.py
            │   ├── static/
            │   │   ├── css/         # Estilos (chord-lab, piano, layout)
            │   │   └── js/          # Scripts (chord-lab, piano, ports)
            │   └── view/templates/
            │       ├── chord-lab.html
            │       ├── piano.html
            │       └── layout.html
            └── tkinter/
                ├── tk_app.py        # Interface desktop Tkinter
                └── window.py
```

---

## Funcionalidades

- Reprodução de notas MIDI via portas conectadas usando `mido` e `python-rtmidi`
- Piano visual interativo na interface web
- Chord Lab para explorar e tocar acordes pelo navegador
- Seleção de porta MIDI disponível em todas as abas da interface
- Multiplas interfaces: CLI, web (Flask) e desktop (Tkinter)
- Arquitetura limpa com separação clara entre domínio, aplicação e infraestrutura

---

## Tecnologias

| Camada | Tecnologia |
|---|---|
| Backend MIDI | mido + python-rtmidi |
| Interface Web | Flask + Jinja2 |
| Interface Desktop | Tkinter |
| CLI | Python |
| Linguagem | Python 3.12 |

---

## Como Executar

### Pre-requisitos

- Python 3.10 ou superior
- Porta MIDI virtual ou dispositivo MIDI físico (opcional)

### Instalacao

```bash
# Clonar o repositório
git clone https://github.com/nearo007/MIDI_project.git
cd MIDI_project

# Criar e ativar o ambiente virtual
python -m venv venv

# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### Execucao

**Aplicação web Flask (recomendado):**
```bash
python main.py
```
Acesse `http://localhost:5000` no navegador.

**CLI:**
```bash
python src/infrastructure/ui/cli/cli_app.py
```

**Interface desktop Tkinter:**
```bash
python src/infrastructure/ui/tkinter/tk_app.py
```

---

## Dependencias

```
flask
mido
python-rtmidi
```

Instale todas com:
```bash
pip install -r requirements.txt
```

---

## Branches

| Branch | Descrição |
|---|---|
| `main` | Código estável |
| `simplifying-structure` | Refatoração e melhorias estruturais |
| `web-application-set-up` | Configuração inicial da aplicação web |

---

## Autor

**nearo007** - [GitHub](https://github.com/nearo007)
