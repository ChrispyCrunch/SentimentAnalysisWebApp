from nicegui import ui
from Predict import Predict

@ui.page('/')
def home():
    prediction = Predict()

    ui.add_body_html("""
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Lexend+Mega:wght@100..900&display=swap" rel="stylesheet">""")
    
    font = 'font-family: "Lexend Mega", sans-serif; font-optical-sizing: auto; font-weight: 700; font-style: normal;'

    def handle_button(e):
        if e.value:
            try:
                result_view.clear()
                result, score = prediction.make_prediction(e.value)
                if result:
                    score = f"I'm {round(float(score) * 100)}% sure."
                    with result_view:
                        if result == "positive":
                            ui.icon('thumb_up', color='#50d71e').classes('text-5xl')
                            ui.label('Positive').style(font).classes('text-2xl')
                            ui.label(f"{score}").style(font).classes('text-xl')
                        elif result == "negative":
                            ui.icon('thumb_down', color='#FF4911').classes('text-5xl')
                            ui.label('Negative').style(font).classes('text-2xl')
                            ui.label(f"{score}").style(font).classes('text-xl')
                        elif result == "neutral":
                            ui.icon('sentiment_neutral', color='#3300FF').classes('text-5xl')
                            ui.label('Neutral').style(font).classes('text-2xl')
                            ui.label(f"{score}").style(font).classes('text-xl') 
            except Exception as e:
                ui.icon('error', color='red').classes('text-5xl')
                ui.label(f"{e}") 
            finally:
                result_view.set_visibility(True)
    
    ui.query('body').classes('bg-cyan-500')

    with ui.row().classes('items-center flex h-screen m-auto'):
        with ui.card().classes('border-solid border-4 border-black max-w-3xl').style('box-shadow: 10px 10px 0px 10px #000000;'):
            with ui.column().classes('items-center text-center text-wrap'):
                with ui.row():
                    ui.label('Sentiment Analysis').classes('text-4xl').style(font)
                with ui.row().classes('bg-[#FFFF00] mb-1'):
                    ui.label("Easily decode the emotions behind your text with this Sentiment Analysis Tool. "
                            "Just type or paste your text, hit the button, and unveil the sentiment—positive, negative, "
                            "or neutral—in seconds.").style(font)
                with ui.row():
                    user_input = ui.textarea(placeholder='Paste the text you want to perform sentiment analysis on...').style('width: 50em').classes('border-solid border-4 border-black px-1').props('color=fuchsia-600')
                with ui.row():
                    ui.button('Check sentiment', color='fuchsia-600', on_click=lambda: handle_button(user_input)).classes('border-solid border-4 border-black text-xl').style(font)
            with ui.card_section().classes('w-full items-center'):
                with ui.column().classes('items-center') as result_view:
                    result_view.set_visibility(False)
                

print('\nIf this is your first time running, the model will be downloaded from huggingface, please standby.\n')
ui.run(title="Sentiment Analysis")
