import matplotlib.pyplot as plt
import matplotlib.widgets

fig, (ax,sliderax) = plt.subplots(nrows=2,gridspec_kw=dict(height_ratios=[1,.05]))

ax.plot(range(11))
ax.set_xlim(5,None)
ax.set_title("Type number to set minimum slider value")
def update_range(val):
    ax.set_xlim(val,None)

def update_slider(evt):
    print(evt.key)
    try:
        val = int(evt.key)
        slider.valmin = val
        slider.ax.set_xlim(slider.valmin,None)
        if val > slider.val:
            slider.val=val
            update_range(val)
        fig.canvas.draw_idle()
    except:
        pass

slider=matplotlib.widgets.Slider(sliderax,"xlim",0,10,5)
slider.on_changed(update_range)

fig.canvas.mpl_connect('key_press_event', update_slider)

plt.show()