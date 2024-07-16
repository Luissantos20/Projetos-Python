# Passo a passo

# Título: Hashzap
# Botão: Iniciar chat
    # popup/modal/alerta
        # Campo  de Texto: Escreva seu noome no chat
        # Botão: Entrar no chat
            # Sumir com o título e o Botão inicial
            # Fechar o popup
            # Criar o char ( com a mensagem de "nome do usuário entrou no chat")
            # Embaixo do chat:
                # Campo de texto: Digite sua mensagem
                # Botão Enviar
                    # Vai aparecer a mensagem co o nome do usuário no site
                    # Lira: Coe galera


# Flet

import flet as ft

# criar a funçao principal do seu sistema
def main(pagina):
    # criar
    titulo = ft.Text("Hashzap")

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)


    titulo_janela = ft.Text("Bem vindo ao Hashzap")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")

    

    def enviar_mensagem(evento):
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"

        
        texto_mensagem.value = ""

        pagina.pubsub.send_all(texto)

        pagina.update()

    texto_mensagem = ft.TextField(label="Digite sua mensagem")
    botao_enviar =  ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    chat = ft.Column()

    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])
    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        texto_mensagem = ft.TextField(label="Digite sua mensagem")
        pagina.add(linha_mensagem)
        pagina.add(chat)
        

        texto_entrou_chat = f"{campo_nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto_entrou_chat)
        pagina.update()

    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome_usuario,
        actions=[botao_entrar],
    )

    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()


    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    #adicionar
    pagina.add(titulo)
    pagina.add(botao_iniciar)


# executar o seu sistema
ft.app(main, view=ft.WEB_BROWSER)