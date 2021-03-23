![https://static-2.gumroad.com/res/gumroad-public-storage/variants/x6bida3j2nm6olyl4tjcw9cz7qga/863e71bca49b1d996cbba6a1171aa48abf862c5dc070868836b79f346192c66f](https://static-2.gumroad.com/res/gumroad-public-storage/variants/x6bida3j2nm6olyl4tjcw9cz7qga/863e71bca49b1d996cbba6a1171aa48abf862c5dc070868836b79f346192c66f)
# About
I made these little entries to streamline the workflow of visibility and rendering, because when working with many objects, the render visibility sometimes is not the same as the viewport visibility. When you hit render, things are hidden or shown accidentally, ruining good renders - the final Render output is the important one. The viewport should reflect that. This is a visibility quality check UX.

# Features:
Adds a Match Visibility panel to the Properties Shelf>View tab from 3D View
Adds a drop down to the Filter panel to match visibility from Outliner
Press a "Show Render Only" button to see final render results in the viewport (hides overlays and matches render display settings to viewport. CTRL+Z to revert.
Match from view (updates viewport and render to hide settings)
Match from viewport (updates render and view to viewport settings)
Match from render (updates view and viewport to render settings)
Updates

**[Ver 1.0.6]**
- Fixed: removed a bug that would try to iterate all the objects in all the scenes, instead of only in the active scene as it should. Naughty boy.

**[Ver 1.0.5]**
Updates to 1.0.5: Uploaded wrong version......Doh! Again. This is my first addon.. thanks for all the patience.

**[Ver 1.0.4]**
- Fix: wasn't installing to Blender because the outliner has no view menu. Doh! Bforartists yes. I have now moved the operators in the outliner to the filter menu. The 3D View panel is still the same.

**[1.0.3]**
- Added the ability to check collection viewport and render visibility.
- Added Show Render only so that it hides overlays, widgets, and shows only render object and collections.
- Add the ability to match from object hidden visibility
- Improved tooltips and UI entries.

**Links:**
https://github.com/Draise14/Addon-Match-to-Render

# Use

To update the viewport to final render visibility or vice versa (render visibility to viewport), you can use the addon to see what is shown for final render.

1. Download
2. Install using the Blender/Bforartists addon installation process
3. Use the panel in the View tab or under the 3D View>View hearder entries
4. Use in the Outliner Filter Panel

## What you get:
A python script you can install as an addon in Blender 2.8+ (also works with 2.9+ builds)
