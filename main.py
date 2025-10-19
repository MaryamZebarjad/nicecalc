from nicegui import ui
ui.colors(asli='#C13DC1',rang2='#2CA0D2')


#--------------------------------------------------------------------------------------------------------------------------------------       
                                                              # ماشین حساب
#--------------------------------------------------------------------------------------------------------------------------------------
btns = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+']
]

def keyboard(n):
    if n=='=':
        if inp.value:
            try:
                inp.value=eval(inp.value)
            except:
                ui.notify('خطا در محاسبه')
        else:
            ui.notify('اذیت نکن')
    elif n in ['+','-','*','/']:
        if inp.value:
            inp.value=(inp.value or '')+n
        else:
            ui.notify('اول عدد بنویس')  
    elif n in ['0','.']:
        if inp.value:
            inp.value=(inp.value or '')+n
        else:
            inp.value='0.' if n=='.' else '0'   
    else:
        inp.value=(inp.value or '')+n
    
with ui.row().classes('w-full h-screen items-center justify-center'):
    with ui.column().classes('gap-1 items-center justify-center'):
        inp=ui.input().props('clearable outlined color=idigo-10').style('width:44vh;font-size:40px;')
        for row in btns:
            with ui.row().classes('w-full gap-1'):
                for btn in row:
                    if btn in['-','+','*','/','0','=','.']:
                        ui.button(btn,on_click=lambda b=btn:keyboard(b)).props('unelevated color=indigo-4').style('width:10.6vh;height:10.6vh;')
                    else:
                        ui.button(btn,on_click=lambda b=btn:keyboard(b)).props('unelevated color=indigo-3').style('width:10.6vh;height:10.6vh;')

ui.run(title='SimpleCalculator',host='0.0.0.0',port=8080)
