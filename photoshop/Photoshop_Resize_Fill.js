#target photoshop
app.preferences.rulerUnits = Units.PIXELS;
var docRef = activeDocument;
var size = 1024;
docRef.width>docRef.height ? docRef.resizeImage(undefined, size, undefined) : docRef.resizeImage(size, undefined, undefined);
app.activeDocument.resizeCanvas(UnitValue(size,"px"),UnitValue(size,"px"));