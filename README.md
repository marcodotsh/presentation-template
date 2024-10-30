# Reveal.js slides template

A simple template for reveal.js presentations. To start a presentation you need to have a simple http server running. To set this up, you can run 

```
python3 -m http.server
```

for example.

This template includes all of the standard reveal.js plugins as well as the [manim-revealjs plugin](http://github.com/RickDW/manim-revealjs). This plugin makes it easy to use the [Manim](http://www.manim.community) animation software for your presentations.

# How to use
`presentation.md`: use this file to create the presentation
`scenes.py`: use this file to create Manim Scenes
To generate Manim animations (e.g. DemoScene) run
```
manim render scenes.py DemoScene
```
