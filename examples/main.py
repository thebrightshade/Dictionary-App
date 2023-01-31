import justpy as jp

@jp.SetRoute("/home")
def home():
    wp = jp.WebPage()
    div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
    div1 = jp.Div(a=div, classes="grid grid-cols-3 gap-4")
    in_1 = jp.Input(a=div1, 
            placeholder="Enter first value",
            classes="form-input")
    in_2 = jp.Input(a=div1, 
            placeholder="Enter second value",
            classes="form-input")
    d_output = jp.Div(a=div1, text='Result goes here...',
            classes="border text-gray-600")
    jp.Div(a=div1, text='Another Div...',
            classes="border text-gray-600")
    jp.Div(a=div1, text='Yet Another Div...',
            classes="border text-gray-600")
    div2 = jp.Div(a=div, classes="grid grid-cols-2 gap-4")
    jp.Button(a=div2, text='Calculate', click=sum_up, 
                in1=in_1, in2=in_2, d=d_output,
                classes='border border-blue-500 m-2 p-2 '
                        'rounded text-blue-600 '
                        'hover:bg-red-300 hover:text-white')
    jp.Div(a=div2, text='Cool Div',
            classes="border text-gray-600 "
                    "border border-blue-500 "
                    "m-2 p-2 "
                    "hover:bg-green-500 hover:text-blue-200",
                    mouseenter=mouse_enter,
                    mouseleave=mouse_left)
    return wp

def sum_up(widget, msg): #widget: Button(id: 3, html_tag: button, vue_type: html)
    summed_value =  float(widget.in1.value)+float(widget.in2.value)
    widget.d.text = summed_value

def mouse_enter(widget, msg):
    widget.text="Mouse entered the box!"

def mouse_left(widget, msg):
    widget.text="Mouse left the box!"




jp.justpy()
