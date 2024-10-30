import manim as mn
from manim_revealjs import PresentationScene, NORMAL, LOOP, COMPLETE_LOOP, NO_PAUSE


mn.config.video_dir= "./animations"

class DemoScene(PresentationScene):
    def construct(self):
        rect = mn.Rectangle(fill_color=mn.BLUE, fill_opacity=1)
        self.play(mn.Create(rect))
        self.end_fragment()

        self.play(rect.animate.shift(mn.UP).rotate(mn.PI / 3))
        self.play(rect.animate.rotate(-mn.PI / 3).shift(mn.DOWN))
        self.end_fragment(fragment_type=COMPLETE_LOOP)

        self.play(rect.animate.shift(mn.UP).rotate(mn.PI / 3))
        self.end_fragment(fragment_type=NO_PAUSE)
        
        self.play(rect.animate.shift(3*mn.LEFT))
        self.end_fragment()

