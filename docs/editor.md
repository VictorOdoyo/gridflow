# Interactive network editor

The GridFlow workbench provides an SVG topology canvas with draggable bus coordinates, selectable buses/branches, equipment tables and a property inspector. Add/delete commands update the native model; deleting a bus removes its attached equipment. Undo keeps the latest 30 edit snapshots in memory. Layout coordinates are presentation data, not impedance lengths or geographic coordinates. Device parameters remain explicit; drawing an edge does not infer cable properties. The advanced JSON editor handles nested matrices, source settings, regulator definitions and study profiles. Imported data is validated before replacing the current model.

Run results belong to a particular model snapshot. Editing invalidates export/print of the old result and clears its diagram overlays. Browser network drafts persist locally; exported JSON is the durable interchange format. The browser makes no external analytics or solver requests.
