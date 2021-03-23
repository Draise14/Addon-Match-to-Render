################### About ###################

# I made these little entries to streamline the workflow of visibility and rendering, 
# because when working with many objects, the render visibilty sometimes is not the 
# same as the viewport visibility, and when you hit render, things are hidden or shown
# accidentally, ruining good renders. This is a quality check UX. 
# To update the viewport to final render or vice versa (render to viewport), 
# you can use the script to see what is what for final render. 

# Update: fixed a blender registration bug to make it compatible to BFA


################### Preliminary Information ###################
bl_info = {
    "name": "Match Render Visibility",
    "author": "Andres (Draise) Stephens",
    "version": (1, 0, 5),
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

class OUTLINER_MT_renderview(Menu):
    bl_label = "Match Render Visibility"
    def draw(self, context):
        layout = self.layout

# NOTE: I'd love to control the 3D view "Show Render Only" from here, but not sure how. 
# Might add an option in the addon later to control where you'd like to add this menu, if in the 3D View with the other operator, or here in the outliner where it would make sense - yet still be able to control the viewport. 

        #layout.operator(VIEW3D_OT_showrender.bl_idname, text="Show Render Only", icon = "OVERLAY")
        
        layout.separator()
        layout.operator(VIEW3D_OT_update_view_to_render.bl_idname, text="from Render", icon = "RESTRICT_RENDER_OFF")
        layout.operator(VIEW3D_OT_update_render_to_view.bl_idname, text="from Viewport", icon = "RESTRICT_VIEW_OFF")
        layout.operator(VIEW3D_OT_gethide.bl_idname, text="from Hidden", icon = "HIDE_OFF")



################### Register the UI entries ###################

# Panel Entries in Properties Shelf
class VIEW3D_PT_rendervisibility(bpy.types.Panel):
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


# Header Entries in Outliner

def drawmenu(self, context):    
    layout = self.layout
    layout.separator()
    layout.menu("OUTLINER_MT_renderview")    


################### Classes ###################

# ------------------- Registering classes. The classes tuple.
classes = (
    VIEW3D_OT_update_view_to_render,
    VIEW3D_OT_update_render_to_view,
    VIEW3D_OT_gethide,
    VIEW3D_OT_showrender,
    OUTLINER_MT_renderview,
    VIEW3D_PT_rendervisibility,
)

# ------------------- Register Unregister

def register():
    bpy.utils.register_class(VIEW3D_OT_update_view_to_render)
    bpy.utils.register_class(VIEW3D_OT_update_render_to_view)
    bpy.utils.register_class(VIEW3D_OT_gethide)
    bpy.utils.register_class(VIEW3D_OT_showrender)
    bpy.utils.register_class(OUTLINER_MT_renderview)
    bpy.utils.register_class(VIEW3D_PT_rendervisibility)
    bpy.types.OUTLINER_PT_filter.prepend(drawmenu)
    
def unregister():
    bpy.utils.unregister_class(VIEW3D_OT_update_view_to_render)
    bpy.utils.unregister_class(VIEW3D_OT_update_render_to_view)
    bpy.utils.unregister_class(VIEW3D_OT_gethide)
    bpy.utils.unregister_class(VIEW3D_OT_showrender)
    bpy.utils.unregister_class(OUTLINER_MT_renderview)
    bpy.utils.unregister_class(VIEW3D_PT_rendervisibility)
    bpy.types.OUTLINER_PT_filter.remove(drawmenu)
    
    
# For scripting only
if __name__ == "__main__":
    register()