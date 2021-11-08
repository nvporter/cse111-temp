import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()
'''
def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
   
    tree_center = scene_left + 500
    tree_top = scene_top + 100
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)
'''
def draw_ground(canvas, topLeft, bottomRight):
    canvas.create_rectangle(
        topLeft[0], topLeft[1], bottomRight[0], bottomRight[1],
        outline = 'green', fill = 'green')
def draw_cloud(canvas, topLeft, bottomRight):
    canvas.create_oval(
        topLeft[0], topLeft[1], bottomRight[0], bottomRight[1],
        outline = 'black', fill = 'white'
    )
def draw_mountain(canvas, x_position, size, fill = 'light gray'):
    canvas.create_polygon(x_position -200 * size , 400, x_position, 100-(300*(size-1)) , x_position + 200 * size, 400 , 
    outline = 'gray', fill = fill
    )
def draw_background(canvas, topLeft, bottomRight):
    canvas.create_rectangle(topLeft, bottomRight,
    outline = "light blue" , fill = 'light blue')

def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    tree_center = scene_left + 600
    tree_top = scene_top + 300
    tree_height = 150
    draw_background(canvas, (0,0),(800,500))
    draw_ground(canvas, (0, scene_bottom - 100), (scene_right, scene_bottom))
    draw_mountain(canvas, 200, 1.2, fill = 'gray')
    draw_mountain(canvas, 700, 2 , fill='gray')
    draw_mountain(canvas, 550, .9, fill= 'light gray')
    draw_cloud(canvas, (100,50), (250,120) )
    draw_cloud(canvas, (350, 100), (650,200 ))
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    draw_pine_tree(canvas, 100, 300, 200)
    draw_pine_tree(canvas, 250, 300, 100)
    draw_pine_tree(canvas, 300, 300, 175)

    



def draw_pine_tree(canvas, peak_x, peak_y, height):
    
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")




    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")



# Call the main function so that
# this program will start executing.
main()