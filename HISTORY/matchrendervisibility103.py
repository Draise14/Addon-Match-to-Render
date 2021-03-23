################### About ###################

# I made these little entries to streamline the workflow of visibility and rendering, 
# because when working with many objects, the render visibilty sometimes is not the 
# same as the viewport visibility, and when you hit render, things are hidden or shown
# accidentally, ruining good renders. This is a quality check UX. 
# To update the viewport to final render or vice versa (render to viewport), 
# you can use the script to see what is what for final render. 

# Update: fixed the file name to work


################### Preliminary Information ###################
bl_info = {
    "name": "Match Render Visibility",
    "author": "Andres (Draise) Stephens",
    "version": (1, 0, 3),
    "blender": (2, 80, 0),
    "location": "View3D > Properties Shelf > View > Viewport to Render Visibility",
    "description": "Operators to Show Render only and other visibility matching controls.", 
    "warning": "",
    "doc_url": "https://github.com/Draise14/Addon-Match-to-Render",
    "category": "View",
}

import bpy
from bpy.types import (
    Header,
    Menu,
    Panel,
    BoolProperty,
)


################### Operators ###################

# First Operator 
class VIEW3D_OT_update_view_to_render(bpy.types.Operator):
    """Match all visibility toggles to render visibility
    This includes Collections"""
    bl_idname = "update_view_to_render.renderto"
    bl_label = "Match to Render"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        print("Operator is executing")
        for x in bpy.data.objects:
            print(x, "listed")
            if x.hide_render == True:
                x.hide_viewport = True
                x.hide_set(True)
            else:
                if x.hide_render == False:
                    x.hide_viewport = False
                    x.hide_set(False)
        for x in bpy.data.collections:
            if x.hide_render == True:
                x.hide_viewport = True
            else:
                if x.hide_render == False:
                    x.hide_viewport = False
        print("Operator Finished, now all is set")
        return {'FINISHED'}
    
# Second Operator
class VIEW3D_OT_update_render_to_view(bpy.types.Operator):
    """Match all visibility toggles to viewport visibility
    This includes Collections"""
    bl_idname = "update_view_to_render.viewto"
    bl_label = "Match to Viewport"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        print("Operator is executing")
        for x in bpy.data.objects:
            print(x, "listed")
            if x.hide_viewport == True:
                x.hide_render = True
                x.hide_set(True)
                print (x, "render to view done")
            else:
                if x.hide_viewport == False:
                    x.hide_render = False
                    x.hide_set(False)
                    print (x, "visibility is True") 
        for x in bpy.data.collections:
            if x.hide_viewport == True:
                x.hide_render = True
                #print (x, "view to render done")
            else:
                if x.hide_viewport == False:
                    x.hide_render = False
        print("Operator Finished, now all is set")    
        return {'FINISHED'}

# Third Operator
class VIEW3D_OT_gethide(bpy.types.Operator):
    """Match all visibility toggles to hide visibility
    This doesn't affect Collection"""
    bl_idname = "update_view_to_render.gethide"
    bl_label = "Match to Hidden"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        print("Operator is executing")
        for x in bpy.data.objects:
            #print(x, x.hide_get())
            if x.hide_get() == True:
                x.hide_viewport = True 
                x.hide_render = True
            else:
                if x.hide_get() == False:
                    x.hide_viewport = False 
                    x.hide_render = False     
        for x in bpy.data.objects:
            #print(x, x.hide_get())
            if x.hide_get() == True:
                x.hide_viewport = True 
                x.hide_render = True
            else:
                if x.hide_get() == False:
                    x.hide_viewport = False 
                    x.hide_render = False     
        print("Operator Finished, now all is set - except for those pesky collection hide toggles")    
        return {'FINISHED'}
        
# Fourth Operator
class VIEW3D_OT_showrender(bpy.types.Operator):
    """Show Render Result in Viewport"""
    bl_idname = "update_view_to_render.showrender"
    bl_label = "Show Render in Viewport"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        print("Operator is executing")
        for x in bpy.data.objects:

            bpy.context.space_data.overlay.show_overlays = False
            bpy.context.space_data.shading.type = 'RENDERED'
            bpy.context.space_data.show_gizmo = False

            if x.hide_render == True:
                x.hide_viewport = True
                x.hide_set(True)
            else:
                if x.hide_render == False:
                    x.hide_viewport = False
                    x.hide_set(False)
        for x in bpy.data.collections:
            if x.hide_render == True:
                x.hide_viewport = True
            else:
                if x.hide_render == False:
                    x.hide_viewport = False
        return {'FINISHED'}



################### Register the Submenu UI entries ###################

class VIEW3D_MT_render_visibility(Menu):
    bl_label = "Render Visibility"
    def draw(self, _context):
        layout = self.layout
        layout.operator(VIEW3D_OT_showrender.bl_idname, text="Show Render Only", icon = "OVERLAY")
        layout.separator()
        layout.operator(VIEW3D_OT_update_view_to_render.bl_idname, text="Match from Render", icon = "RESTRICT_RENDER_OFF")
        layout.operator(VIEW3D_OT_update_render_to_view.bl_idname, text="Match from Viewport", icon = "RESTRICT_VIEW_OFF")
        layout.operator(VIEW3D_OT_gethide.bl_idname, text="Match from Hidden", icon = "HIDE_OFF")


################### Register the UI entries ###################

# Panel Entries in Properties Shelf
class UpdateViewToRender(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_update_view_to_render"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "View"
    bl_label = "Render Visibility"
        
    
    def draw(self, context):    
        layout = self.layout
        
        # Show Render Button
        row = layout.row()
        row.operator(VIEW3D_OT_showrender.bl_idname, text="Show Render Only", icon = "OVERLAY")

        # Math From Box
        box = layout.box()
        col = box.column(align=True)
        
        col.label(text="Match from:")
        layout.use_property_split = False
        
        col.operator(VIEW3D_OT_update_view_to_render.bl_idname, text="Render", icon = "RESTRICT_RENDER_OFF")
        col.operator(VIEW3D_OT_update_render_to_view.bl_idname, text="Viewport", icon = "RESTRICT_VIEW_OFF")
        col.operator(VIEW3D_OT_gethide.bl_idname, text="Hidden", icon = "HIDE_OFF")


# Header Entries in View Header Menu 
# location: 3D View>View in Blender
# location: Outliner>View in Bforartists
def drawmenu(self, context):    
    layout = self.layout
    layout.separator()
    layout.menu("VIEW3D_MT_render_visibility")    



################### Classes ###################

# ------------------- Registering classes. The classes tuple.
classes = (
    VIEW3D_OT_update_view_to_render,
    VIEW3D_OT_update_render_to_view,
    VIEW3D_OT_gethide,
    VIEW3D_OT_showrender,
    VIEW3D_MT_render_visibility,
    UpdateViewToRender,
)

# ------------------- Register Unregister

def register():
    bpy.utils.register_class(VIEW3D_OT_update_view_to_render)
    bpy.utils.register_class(VIEW3D_OT_update_render_to_view)
    bpy.utils.register_class(VIEW3D_OT_gethide)
    bpy.utils.register_class(VIEW3D_OT_showrender)
    bpy.utils.register_class(VIEW3D_MT_render_visibility)
    bpy.utils.register_class(UpdateViewToRender)
    if bpy.types.OUTLINER_MT_view.is_registered == True:
        bpy.types.OUTLINER_MT_view.append(drawmenu)
    else:
        bpy.types.VIEW3D_MT_view.append(drawmenu)


def unregister():
    bpy.utils.unregister_class(VIEW3D_OT_update_view_to_render)
    bpy.utils.unregister_class(VIEW3D_OT_update_render_to_view)
    bpy.utils.unregister_class(VIEW3D_OT_gethide)
    bpy.utils.unregister_class(VIEW3D_OT_showrender)
    bpy.utils.unregister_class(VIEW3D_MT_render_visibility)
    bpy.utils.unregister_class(UpdateViewToRender)
    if bpy.types.OUTLINER_MT_view.is_registered == True:
        bpy.types.OUTLINER_MT_view.remove(drawmenu)
    else:
        bpy.types.VIEW3D_MT_view.remove(drawmenu)

    
    
# For scripting only
if __name__ == "__main__":
    register()