import tkinter as tk
from tkinter import messagebox, ttk

from Controller.app_controller import AppController


CORES = {
    "fundo": "#edf7f2",
    "painel": "#ffffff",
    "painel_suave": "#f7fbf9",
    "primaria": "#1f8a70",
    "primaria_escura": "#146052",
    "secundaria": "#25435b",
    "texto": "#1d2b34",
    "texto_suave": "#60727d",
    "borda": "#cfe1d9",
    "alerta": "#fff7e6"
}


class GeneMapApp:
    def __init__(self):
        self.controller = AppController()
        self.janela = tk.Tk()
        self.janela.title("GeneMap")
        self.janela.geometry("960x660")
        self.janela.minsize(840, 590)
        self.janela.configure(bg=CORES["fundo"])

        self.nome_var = tk.StringVar()
        self.idade_var = tk.StringVar()
        self.sexo_var = tk.StringVar(value="Feminino")
        self.doencas_var = tk.StringVar()
        self.pai_var = tk.StringVar()
        self.mae_var = tk.StringVar()
        self.fumante_var = tk.BooleanVar()
        self.sedentario_var = tk.BooleanVar()
        self.membro_analise_var = tk.StringVar()
        self.doencas_analise_var = tk.StringVar()

        self._configurar_estilo()
        self._mostrar_login()

    def _configurar_estilo(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(".", font=("Segoe UI", 10), background=CORES["fundo"], foreground=CORES["texto"])
        estilo.configure("TFrame", background=CORES["fundo"])
        estilo.configure("Card.TFrame", background=CORES["painel"], relief="flat")
        estilo.configure("Hero.TFrame", background=CORES["primaria"])
        estilo.configure("TLabel", background=CORES["fundo"], foreground=CORES["texto"], padding=4)
        estilo.configure("Card.TLabel", background=CORES["painel"], foreground=CORES["texto"], padding=4)
        estilo.configure("Muted.TLabel", background=CORES["painel"], foreground=CORES["texto_suave"])
        estilo.configure("Hero.TLabel", background=CORES["primaria"], foreground="#ffffff")
        estilo.configure("Header.TLabel", font=("Segoe UI", 18, "bold"), background=CORES["fundo"])
        estilo.configure("HeroHeader.TLabel", font=("Segoe UI", 24, "bold"), background=CORES["primaria"], foreground="#ffffff")
        estilo.configure("Subheader.TLabel", font=("Segoe UI", 11, "bold"))

        estilo.configure(
            "TButton",
            padding=(14, 8),
            background=CORES["primaria"],
            foreground="#ffffff",
            borderwidth=0,
            focusthickness=0
        )
        estilo.map(
            "TButton",
            background=[("active", CORES["primaria_escura"]), ("disabled", "#a9bbb3")],
            foreground=[("disabled", "#eef4f1")]
        )
        estilo.configure(
            "Secondary.TButton",
            background=CORES["secundaria"],
            foreground="#ffffff"
        )
        estilo.map("Secondary.TButton", background=[("active", "#193247")])

        estilo.configure("TEntry", fieldbackground="#ffffff", bordercolor=CORES["borda"], padding=7)
        estilo.configure("TCombobox", fieldbackground="#ffffff", bordercolor=CORES["borda"], padding=7)
        estilo.configure("TCheckbutton", background=CORES["painel"], foreground=CORES["texto"])

        estilo.configure(
            "TLabelframe",
            background=CORES["painel"],
            bordercolor=CORES["borda"],
            relief="solid"
        )
        estilo.configure(
            "TLabelframe.Label",
            background=CORES["painel"],
            foreground=CORES["primaria_escura"],
            font=("Segoe UI", 11, "bold")
        )

        estilo.configure("TNotebook", background=CORES["fundo"], borderwidth=0)
        estilo.configure(
            "TNotebook.Tab",
            padding=(18, 10),
            background="#dbece5",
            foreground=CORES["secundaria"]
        )
        estilo.map(
            "TNotebook.Tab",
            background=[("selected", CORES["primaria"])],
            foreground=[("selected", "#ffffff")]
        )

        estilo.configure(
            "Treeview",
            background="#ffffff",
            fieldbackground="#ffffff",
            foreground=CORES["texto"],
            rowheight=28,
            bordercolor=CORES["borda"],
            borderwidth=1
        )
        estilo.configure(
            "Treeview.Heading",
            background=CORES["secundaria"],
            foreground="#ffffff",
            font=("Segoe UI", 10, "bold"),
            padding=6
        )
        estilo.map("Treeview", background=[("selected", CORES["primaria"])], foreground=[("selected", "#ffffff")])

    def _limpar_janela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

    def _criar_card(self, pai, padding=18):
        card = ttk.Frame(pai, style="Card.TFrame", padding=padding)
        card.configure(style="Card.TFrame")
        return card

    def _mostrar_login(self):
        self._limpar_janela()

        externo = ttk.Frame(self.janela, padding=34)
        externo.pack(fill="both", expand=True)

        card = self._criar_card(externo, padding=0)
        card.place(relx=0.5, rely=0.5, anchor="center", width=520, height=430)

        hero = ttk.Frame(card, style="Hero.TFrame", padding=24)
        hero.pack(fill="x")

        ttk.Label(hero, text="GeneMap", style="HeroHeader.TLabel").pack(anchor="w")
        ttk.Label(hero, text="Mapeamento familiar e alertas genéticos preventivos", style="Hero.TLabel").pack(anchor="w")

        corpo = ttk.Frame(card, style="Card.TFrame", padding=28)
        corpo.pack(fill="both", expand=True)

        ttk.Label(corpo, text="Usuário", style="Card.TLabel").pack(anchor="w")
        usuario = ttk.Entry(corpo, width=38)
        usuario.pack(fill="x", pady=(0, 10))

        ttk.Label(corpo, text="Senha", style="Card.TLabel").pack(anchor="w")
        senha = ttk.Entry(corpo, width=38, show="*")
        senha.pack(fill="x", pady=(0, 14))

        botoes = ttk.Frame(corpo, style="Card.TFrame")
        botoes.pack(fill="x", pady=(2, 12))

        ttk.Button(
            botoes,
            text="Entrar",
            command=lambda: self._login(usuario.get(), senha.get())
        ).pack(side="left", fill="x", expand=True, padx=(0, 6))
        ttk.Button(
            botoes,
            text="Cadastrar",
            style="Secondary.TButton",
            command=lambda: self._cadastrar_usuario(usuario.get(), senha.get())
        ).pack(side="left", fill="x", expand=True, padx=(6, 0))

        ttk.Label(corpo, text="Usuário inicial: admin | Senha: admin", style="Muted.TLabel").pack(anchor="center")
        usuario.focus()

    def _login(self, usuario, senha):
        if self.controller.autenticar(usuario, senha):
            self._mostrar_sistema()
            return

        messagebox.showerror("Login", "Usuário ou senha inválidos.")

    def _cadastrar_usuario(self, usuario, senha):
        sucesso, mensagem = self.controller.cadastrar_usuario(usuario, senha)

        if sucesso:
            messagebox.showinfo("Cadastro", mensagem)
        else:
            messagebox.showwarning("Cadastro", mensagem)

    def _mostrar_sistema(self):
        self._limpar_janela()

        container = ttk.Frame(self.janela, padding=18)
        container.pack(fill="both", expand=True)

        topo = ttk.Frame(container, style="Hero.TFrame", padding=18)
        topo.pack(fill="x", pady=(0, 14))

        titulos = ttk.Frame(topo, style="Hero.TFrame")
        titulos.pack(side="left", fill="x", expand=True)

        ttk.Label(titulos, text="GeneMap", style="HeroHeader.TLabel").pack(anchor="w")
        ttk.Label(titulos, text="Histórico familiar, análise de padrões e alertas preventivos", style="Hero.TLabel").pack(anchor="w")
        ttk.Button(topo, text="Sair", style="Secondary.TButton", command=self._mostrar_login).pack(side="right")

        abas = ttk.Notebook(container)
        abas.pack(fill="both", expand=True)

        self.aba_familia = ttk.Frame(abas, padding=14)
        self.aba_analise = ttk.Frame(abas, padding=14)
        self.aba_arvore = ttk.Frame(abas, padding=14)

        abas.add(self.aba_familia, text="Entrada de dados")
        abas.add(self.aba_analise, text="Análise")
        abas.add(self.aba_arvore, text="Árvore familiar")

        self._montar_aba_familia()
        self._montar_aba_analise()
        self._montar_aba_arvore()
        self._atualizar_telas()

    def _montar_aba_familia(self):
        formulario = ttk.LabelFrame(self.aba_familia, text="Cadastrar membro", padding=16)
        formulario.pack(side="left", fill="y", padx=(0, 14))

        campos = [
            ("Nome", self.nome_var),
            ("Idade", self.idade_var),
            ("Doenças conhecidas", self.doencas_var),
            ("Pai", self.pai_var),
            ("Mãe", self.mae_var)
        ]

        for linha, (texto, variavel) in enumerate(campos):
            ttk.Label(formulario, text=texto, style="Card.TLabel").grid(row=linha, column=0, sticky="w", pady=3)
            ttk.Entry(formulario, textvariable=variavel, width=34).grid(row=linha, column=1, pady=5, padx=(8, 0))

        ttk.Label(formulario, text="Sexo", style="Card.TLabel").grid(row=5, column=0, sticky="w", pady=3)
        ttk.Combobox(
            formulario,
            textvariable=self.sexo_var,
            values=["Feminino", "Masculino", "Outro"],
            state="readonly",
            width=31
        ).grid(row=5, column=1, pady=5, padx=(8, 0))

        ttk.Checkbutton(formulario, text="Fumante", variable=self.fumante_var).grid(row=6, column=1, sticky="w", pady=(8, 0), padx=(8, 0))
        ttk.Checkbutton(formulario, text="Sedentário", variable=self.sedentario_var).grid(row=7, column=1, sticky="w", padx=(8, 0))
        ttk.Button(formulario, text="Salvar membro", command=self._salvar_membro).grid(row=8, column=0, columnspan=2, sticky="ew", pady=16)

        lista_frame = ttk.LabelFrame(self.aba_familia, text="Membros cadastrados", padding=16)
        lista_frame.pack(side="left", fill="both", expand=True)

        colunas = ("nome", "idade", "sexo", "doencas", "pai", "mae")
        self.tabela_membros = ttk.Treeview(lista_frame, columns=colunas, show="headings", height=16)

        titulos = {
            "nome": "Nome",
            "idade": "Idade",
            "sexo": "Sexo",
            "doencas": "Doenças",
            "pai": "Pai",
            "mae": "Mãe"
        }

        for coluna in colunas:
            self.tabela_membros.heading(coluna, text=titulos[coluna])
            self.tabela_membros.column(coluna, width=110)

        self.tabela_membros.pack(fill="both", expand=True)

    def _montar_aba_analise(self):
        painel = ttk.LabelFrame(self.aba_analise, text="Parâmetros da análise", padding=16)
        painel.pack(fill="x", pady=(0, 12))

        ttk.Label(painel, text="Membro analisado", style="Card.TLabel").grid(row=0, column=0, sticky="w")
        self.combo_membro_analise = ttk.Combobox(painel, textvariable=self.membro_analise_var, state="readonly", width=32)
        self.combo_membro_analise.grid(row=0, column=1, padx=8, pady=5, sticky="w")

        ttk.Label(painel, text="Doenças para verificar", style="Card.TLabel").grid(row=1, column=0, sticky="w")
        ttk.Entry(painel, textvariable=self.doencas_analise_var, width=58).grid(row=1, column=1, padx=8, pady=5, sticky="ew")
        ttk.Button(painel, text="Analisar riscos", command=self._analisar).grid(row=1, column=2, padx=(8, 0))
        painel.columnconfigure(1, weight=1)

        dica = tk.Label(
            self.aba_analise,
            text="Se deixar doenças em branco, o sistema usa as doenças já cadastradas na família.",
            bg=CORES["alerta"],
            fg=CORES["secundaria"],
            font=("Segoe UI", 10),
            padx=12,
            pady=8,
            anchor="w"
        )
        dica.pack(fill="x", pady=(0, 12))

        self.texto_resultado = self._criar_caixa_texto(self.aba_analise, height=20)
        self.texto_resultado.pack(fill="both", expand=True)

    def _montar_aba_arvore(self):
        barra = ttk.Frame(self.aba_arvore)
        barra.pack(fill="x", pady=(0, 10))

        ttk.Button(barra, text="Atualizar árvore", command=self._atualizar_arvore).pack(anchor="w")
        self.texto_arvore = self._criar_caixa_texto(self.aba_arvore, height=24)
        self.texto_arvore.pack(fill="both", expand=True)

    def _criar_caixa_texto(self, pai, height):
        return tk.Text(
            pai,
            height=height,
            wrap="word",
            bg="#ffffff",
            fg=CORES["texto"],
            insertbackground=CORES["primaria"],
            relief="solid",
            bd=1,
            padx=14,
            pady=12,
            font=("Consolas", 10),
            highlightthickness=1,
            highlightbackground=CORES["borda"],
            highlightcolor=CORES["primaria"]
        )

    def _salvar_membro(self):
        sucesso, mensagem = self.controller.adicionar_membro(
            nome=self.nome_var.get(),
            idade=self.idade_var.get(),
            sexo=self.sexo_var.get(),
            doencas=self.doencas_var.get(),
            pai=self.pai_var.get(),
            mae=self.mae_var.get(),
            fumante=self.fumante_var.get(),
            sedentario=self.sedentario_var.get()
        )

        if not sucesso:
            messagebox.showwarning("Cadastro", mensagem)
            return

        messagebox.showinfo("Cadastro", mensagem)
        self._limpar_formulario()
        self._atualizar_telas()

    def _limpar_formulario(self):
        self.nome_var.set("")
        self.idade_var.set("")
        self.sexo_var.set("Feminino")
        self.doencas_var.set("")
        self.pai_var.set("")
        self.mae_var.set("")
        self.fumante_var.set(False)
        self.sedentario_var.set(False)

    def _atualizar_telas(self):
        self._atualizar_tabela()
        self._atualizar_combo_analise()
        self._atualizar_arvore()

    def _atualizar_tabela(self):
        for item in self.tabela_membros.get_children():
            self.tabela_membros.delete(item)

        for indice, membro in enumerate(self.controller.listar_dados_membros()):
            tag = "par" if indice % 2 == 0 else "impar"
            self.tabela_membros.insert(
                "",
                "end",
                values=(
                    membro["nome"],
                    membro["idade"],
                    membro["sexo"],
                    ", ".join(membro["doencas"]),
                    membro["pai"],
                    membro["mae"]
                ),
                tags=(tag,)
            )

        self.tabela_membros.tag_configure("par", background="#ffffff")
        self.tabela_membros.tag_configure("impar", background=CORES["painel_suave"])

    def _atualizar_combo_analise(self):
        nomes = self.controller.listar_membros()
        self.combo_membro_analise["values"] = nomes

        if nomes and not self.membro_analise_var.get():
            self.membro_analise_var.set(nomes[0])

    def _atualizar_arvore(self):
        self.texto_arvore.delete("1.0", tk.END)

        membros = self.controller.listar_dados_membros()

        if not membros:
            self.texto_arvore.insert(tk.END, "Nenhum membro cadastrado.")
            return

        for membro in membros:
            self.texto_arvore.insert(
                tk.END,
                f"Nome: {membro['nome']}\n"
                f"Idade: {membro['idade']} | Sexo: {membro['sexo']}\n"
                f"Pai: {membro['pai'] or 'Não informado'}\n"
                f"Mãe: {membro['mae'] or 'Não informado'}\n"
                f"Doenças: {', '.join(membro['doencas']) or 'Nenhuma'}\n"
                f"Hábitos de risco: {self._formatar_habitos(membro)}\n"
                "----------------------------------------\n"
            )

    def _formatar_habitos(self, membro):
        habitos = []

        if membro["fumante"]:
            habitos.append("fumante")

        if membro["sedentario"]:
            habitos.append("sedentário")

        return ", ".join(habitos) if habitos else "nenhum informado"

    def _analisar(self):
        nome = self.membro_analise_var.get()

        if not nome:
            messagebox.showwarning("Análise", "Cadastre e selecione um membro antes de analisar.")
            return

        resultados = self.controller.analisar(nome, self.doencas_analise_var.get())
        self.texto_resultado.delete("1.0", tk.END)

        if not resultados:
            self.texto_resultado.insert(tk.END, "Nenhum resultado encontrado.")
            return

        for doenca, dados in resultados.items():
            fatores = self._formatar_fatores(dados["fatores"])
            self.texto_resultado.insert(
                tk.END,
                f"Doença: {doenca}\n"
                f"Risco estimado: {dados['risco']}%\n"
                f"Fatores encontrados: {fatores}\n"
                f"Alerta: {dados['alerta']}\n"
                "----------------------------------------\n"
            )

    def _formatar_fatores(self, fatores):
        nomes = {
            "pai": "pai com histórico",
            "mae": "mãe com histórico",
            "avos": "avós com histórico",
            "irmaos": "irmãos com histórico",
            "fumante": "fumante",
            "sedentario": "sedentário",
            "ja_possui": "doença já registrada no membro"
        }
        encontrados = [texto for chave, texto in nomes.items() if fatores.get(chave)]
        return ", ".join(encontrados) if encontrados else "nenhum fator relevante cadastrado"

    def iniciar(self):
        self.janela.mainloop()


def iniciar_interface():
    app = GeneMapApp()
    app.iniciar()
