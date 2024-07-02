from manim import *
from manim_slides import Slide

import numpy as np

class Scene1(Slide):
    
    def construct(self):
        
        title = Tex(r"Line Segment Tracking", font_size=50).shift(DOWN*1.3)
        author = Tex("Andres Rios-Tascon", font_size=40).next_to(title, DOWN, buff=0.6)
        info = Tex("RSE Group Meeting. Dec 13th, 2023", font_size=30).next_to(author, DOWN, buff=0.6)
        
        seal = ImageMobject("./images/PU-white.png").scale_to_fit_height(0.7).to_edge(DOWN, buff=0.5).to_edge(RIGHT, buff=0.5)

        circle_1 = Circle(color=PURE_RED, radius=1.0).shift(UP*1.5).scale_to_fit_width(1)
        circle_2 = circle_1.copy().scale_to_fit_width(1.8)
        circle_3 = circle_1.copy().scale_to_fit_width(2.6)
        circle_4 = circle_1.copy().scale_to_fit_width(3.4)
        circle_5 = circle_1.copy().scale_to_fit_width(4.2)

        initial_objects = [title, author, info, seal, circle_1, circle_2, circle_3, circle_4, circle_5]

        self.play(*[FadeIn(o) for o in initial_objects])

        self.wait(0.1)
        self.next_slide(loop=True)

        n_particles = 30

        for _ in range(3):
            particles = [Dot().move_to(circle_1.get_center()) for _ in range(n_particles)]
            for p in particles:
                p.move_to(circle_1.get_center())
            paths = [TracedPath(p.get_center, dissipating_time=0.3, stroke_opacity=[0, 1]) for p in particles]
            self.add(*paths)
            final_angles = 2*PI*np.random.rand(n_particles)
            self.play(*[p.animate(path_arc=1.5*PI*(np.random.rand()-0.5)).shift(2.1*(RIGHT*np.cos(angle) + UP*np.sin(angle))).scale(0) for p,angle in zip(particles, final_angles)] , rate_func=linear)
            self.wait(0.3)
            self.remove(*paths)
            self.remove(*particles)

        self.next_slide()

        irishep_long = Tex(r"{{I}}nstitute for {{R}}esearch and {{I}}nnovation in {{S}}oftware\\for {{H}}igh {{E}}nergy {{P}}hysics", font_size=50).shift(UP*2.5)
        irishep = Tex(r"{{I}}{{R}}{{I}}{{S}}-{{H}}{{E}}{{P}}", font_size=50).shift(UP*3 + LEFT*1)
        irishep_logo = ImageMobject("./images/irishep_logo.png").scale_to_fit_height(0.7).next_to(irishep, RIGHT)
        irishep_map = ImageMobject("./images/irishep_map.png").scale_to_fit_height(6).shift(DOWN*0.7)
        nsf_logo = ImageMobject("./images/nsf_logo.png").scale_to_fit_height(1.3).next_to(irishep, DOWN*3)

        self.play(*[Uncreate(o) for o in initial_objects if o is not seal], FadeOut(seal))
        self.play(FadeIn(irishep_long))

        self.wait(0.1)
        self.next_slide()
        self.play(TransformMatchingTex(irishep_long, irishep))
        self.play(FadeIn(irishep_logo))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(irishep_map), FadeIn(nsf_logo))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeOut(irishep_map), FadeOut(nsf_logo))

        main_blist = BulletedList(
            "Analysis Systems",
            "Training, Education and Outreach",
            "Innovative Algorithms",
            "Other (Data Organization, Management and Access (DOMA), OSG-LHC, ...)",
            font_size=35, buff=1.4
        ).next_to(irishep, DOWN, buff=0.7).to_edge(LEFT, buff=1)
        as_blist = BulletedList(
            "Henry (Python packages, build systems, ...)",
            font_size=25,
        ).next_to(main_blist.submobjects[0], DOWN, buff=0.2).to_edge(LEFT, buff=1.5)
        teo_blist = BulletedList(
            "Henry (training material)",
            "Kilian (HSF Training)",
            "Andres (helping out a bit)",
            font_size=25, buff=0.05
        ).next_to(main_blist.submobjects[1], DOWN, buff=0.2).to_edge(LEFT, buff=1.5)
        ia_blist = BulletedList(
            "Kilian (GNN Tracking)",
            "Andres (Line Segment Tracking)",
            font_size=25, buff=0.05
        ).next_to(main_blist.submobjects[2], DOWN, buff=0.2).to_edge(LEFT, buff=1.5)

        self.play(FadeIn(main_blist.submobjects[0]))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(as_blist))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(main_blist.submobjects[1]))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(teo_blist))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(main_blist.submobjects[2]))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(ia_blist))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(main_blist.submobjects[3]))
        self.wait(0.1)
        self.next_slide()
        self.play(Unwrite(main_blist), Unwrite(as_blist), Unwrite(teo_blist), Unwrite(ia_blist), Unwrite(irishep), FadeOut(irishep_logo))

class Scene2(Slide):
    
    def construct(self):

        lst_team = Tex(r"Line Segment Tracking: the team", font_size=50).shift(UP*3)

        main_blist = BulletedList(
            "UCSD",
            "Cornell",
            "U. of Florida",
            "Princeton",
            font_size=35, buff=1.4
        ).next_to(lst_team, DOWN, buff=0.7).to_edge(LEFT, buff=1)
        ucsd = Tex("Jonathan Guiang", ", ", "Slava Krutelyov", r",\\", "Manos Vourliotis", ", ", "Yanxi Gu", ", ", "Avi Yagil", r",\\", "Balaji Venkat Sathia Narayanan", ", ", "Matevz Tadel", tex_environment="flushleft", font_size=25).next_to(main_blist.submobjects[0], DOWN).to_edge(LEFT, buff=1.5)
        cornell = Tex("Gavin Niendorf", ", ", "Peter Wittich", ", ", "Tres Reid", tex_environment="flushleft", font_size=25).next_to(main_blist.submobjects[1], DOWN).to_edge(LEFT, buff=1.5)
        main_blist.submobjects[2].shift(UP*0.5)
        uflorida = Tex("Philip Chang", ", ", "Mayra Silva", tex_environment="flushleft", font_size=25).next_to(main_blist.submobjects[2], DOWN).to_edge(LEFT, buff=1.5)
        main_blist.submobjects[3].shift(UP*1.0)
        princeton = Tex("Peter Elmer", ", ", "Bei Wang", ", ", "Andres Rios-Tascon", tex_environment="flushleft", font_size=25).next_to(main_blist.submobjects[3], DOWN).to_edge(LEFT, buff=1.5)

        world_map = ImageMobject("./images/world_map.png").scale_to_fit_height(3).to_edge(RIGHT, buff=0.5)

        inactive_ucsd = ["Jonathan", "Avi", "Balaji", "Matevz"]
        inactive_cornell = ["Peter", "Tres"]
        inactive_uflorida = ["Philip", "Mayra"]
        inactive_princeton = ["Peter", "Bei"]

        ucsd1 = ucsd.copy()
        cornell1 = cornell.copy()
        uflorida1 = uflorida.copy()
        princeton1 = princeton.copy()
        
        for txt in inactive_ucsd:
            ucsd1.set_color_by_tex(txt, GRAY)
        for txt in inactive_cornell:
            cornell1.set_color_by_tex(txt, GRAY)
        for txt in inactive_uflorida:
            uflorida1.set_color_by_tex(txt, GRAY)
        for txt in inactive_princeton:
            princeton1.set_color_by_tex(txt, GRAY)
        fade_inactive = [ReplacementTransform(ucsd, ucsd1), ReplacementTransform(cornell, cornell1), ReplacementTransform(uflorida, uflorida1), ReplacementTransform(princeton, princeton1)]

        ucsd2 = ucsd1.copy()
        ucsd2.set_color_by_tex("Slava", PURE_RED)
        ucsd3 = ucsd1.copy()
        ucsd3.set_color_by_tex("Manos", PURE_RED)
        ucsd3.set_color_by_tex("Yanxi", PURE_RED)
        ucsd4 = ucsd1.copy()

        cornell2 = cornell1.copy()
        cornell2.set_color_by_tex("Gavin", PURE_RED)
        cornell3 = cornell1.copy()

        princeton2 = princeton1.copy()
        princeton2.set_color_by_tex("Andres", PURE_RED)
        princeton3 = princeton1.copy()
        princeton3.set_color_by_tex("Peter", PURE_RED)

        arrow1 = Arrow(start=ucsd.get_center()+RIGHT*1.1 + UP*0.3, end=RIGHT*1.2 + UP*0.5).set_color(PURE_RED).set_z_index(10)
        arrow2 = Arrow(start=ucsd.get_center()+RIGHT*1.6 + UP*0.05, end=RIGHT*3.4 + UP*0.74).set_color(PURE_RED).set_z_index(10)
        arrow3 = Arrow(start=cornell.get_center()+RIGHT*2.3, end=RIGHT*1.97 + UP*0.77).set_color(PURE_RED).set_z_index(10)
        arrow4 = Arrow(start=princeton.get_center()+RIGHT*2.3, end=RIGHT*1.9 + UP*0.83).set_color(PURE_RED).set_z_index(10)
        arrow5 = Arrow(start=princeton.get_center()+LEFT*1.3, end=RIGHT*1.93 + UP*0.77).set_color(PURE_RED).set_z_index(10)
        blur = ImageMobject("./images/red_blur.png").scale_to_fit_height(2).to_edge(RIGHT, buff=2).shift(UP*0.7)
        
        self.play(FadeIn(lst_team), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(main_blist.submobjects[0]), FadeIn(ucsd))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(main_blist.submobjects[1]), FadeIn(cornell))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(main_blist.submobjects[2]), FadeIn(uflorida))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(main_blist.submobjects[3]), FadeIn(princeton))
        self.wait(0.1)
        self.next_slide()
        self.play(*fade_inactive)
        self.wait(0.1)
        self.next_slide()
        self.play(ReplacementTransform(ucsd1, ucsd2), FadeIn(world_map), Create(arrow1))
        self.wait(0.1)
        self.next_slide()
        self.play(ReplacementTransform(ucsd2, ucsd3), ReplacementTransform(arrow1, arrow2))
        self.wait(0.1)
        self.next_slide()
        self.play(ReplacementTransform(ucsd3, ucsd4), ReplacementTransform(cornell1, cornell2), ReplacementTransform(arrow2, arrow3))
        self.wait(0.1)
        self.next_slide()
        self.play(ReplacementTransform(cornell2, cornell3), ReplacementTransform(princeton1, princeton2), ReplacementTransform(arrow3, arrow4))
        self.wait(0.1)
        self.next_slide()
        self.play(ReplacementTransform(princeton2, princeton3), Uncreate(arrow4))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(blur))
        self.wait(0.1)
        self.next_slide()
        self.add(arrow5)
        self.remove(blur)
        self.wait()
        self.next_slide()
        self.remove(arrow5)
        self.add(blur)
        self.wait(0.1)
        self.next_slide()
        self.play(*[FadeOut(o) for o in [main_blist, ucsd4, cornell3, uflorida1, princeton3, world_map, blur]])
        self.play(Unwrite(lst_team), run_time=0.5)

class Scene3(Slide):

    def construct(self):

        lst_background = Tex(r"Line Segment Tracking: background", font_size=50).shift(UP*3)

        lhc_text = Tex(r"Large Hadron Collider\\(LHC)", font_size=35).to_edge(LEFT, buff=0.4)
        cms_text = Tex(r"Compact Muon Solenoid\\(CMS)", font_size=33).to_edge(RIGHT, buff=0.3)

        lhc_map = ImageMobject("./images/LHC_map.png").scale_to_fit_height(6).shift(DOWN*0.7)

        circle_cw = Circle(radius=1.85).shift(DOWN*0.7).rotate(63*DEGREES)
        circle_cc = Circle(radius=1.85).shift(DOWN*0.7).flip().rotate((-180+63)*DEGREES)
        p1 = Dot().set_color(PURE_RED)
        p2 = p1.copy().set_color(PURE_BLUE)

        cms_coords = 0.8398824245181624*RIGHT + 0.9483620697484811*UP
        circle_cms = Circle(color=BLACK, radius=0.2).move_to(cms_coords)
        dot_explosion = Dot().set_color(BLACK).move_to(cms_coords)

        arrow = Arrow(start=cms_text.get_center()+LEFT*1.7 + UP*0.1, end=cms_coords + RIGHT*0.3).set_color(PURE_RED).set_z_index(10)

        self.play(Write(lst_background), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(lhc_map), Write(lhc_text))
        self.wait()
        self.next_slide(loop=True)
        self.add(p1, p2)
        self.play(MoveAlongPath(p1, circle_cw), MoveAlongPath(p2, circle_cc), rate_func=linear)
        self.wait(1/60)
        self.next_slide(loop=True)
        self.add(circle_cms, arrow, cms_text)
        self.play(MoveAlongPath(p1, circle_cw), MoveAlongPath(p2, circle_cc), dot_explosion.animate.scale(4).set_opacity(0), rate_func=linear)
        self.wait(1/60)
        self.next_slide()

        cms_detector = Tex(r"The CMS Detector", font_size=50).shift(UP*3.5)
        self.play(FadeOut(lst_background), Unwrite(lhc_text), FadeOut(lhc_map), Uncreate(arrow), ReplacementTransform(cms_text, cms_detector), Uncreate(p1), Uncreate(p2), Uncreate(circle_cms))

        cms_image = ImageMobject("./images/cms_detector.png").scale_to_fit_height(5).shift(UP*0.2)
        data_pipeline = Tex(r"{{Raw data $\rightarrow$ Reconstructed data}} $\rightarrow$ Analysis Object Data (AOD)", font_size=35).next_to(cms_image, DOWN, buff=0.5)
        data_pipeline_short = Tex(r"{{Raw data $\rightarrow$ Reconstructed data}}", font_size=35).next_to(cms_image, DOWN, buff=0.5)

        self.play(FadeIn(cms_image))
        self.add(cms_image)
        self.wait(0.1)
        self.next_slide()
        self.play(Write(data_pipeline))
        self.wait(0.1)
        self.next_slide()
        self.play(TransformMatchingTex(data_pipeline, data_pipeline_short))
        self.wait(0.1)
        self.next_slide()
        
        circle1 = Circle(color=PURE_RED, radius=1.0).shift(UP*1.5).scale_to_fit_width(1)
        circle2 = circle1.copy().scale_to_fit_width(1.8)
        circle3 = circle1.copy().scale_to_fit_width(2.6)
        circle4 = circle1.copy().scale_to_fit_width(3.4)
        circle5 = circle1.copy().scale_to_fit_width(4.2)
        circles = [circle1, circle2, circle3, circle4, circle5]

        circle1.shift(4*RIGHT+DOWN*2)
        for c in circles:
            c.scale(0.6)
            c.move_to(circle1.get_center())

        tracker_text = Tex(r"CMS Outer Tracker", font_size=35).next_to(circle5, UP, buff=0.7)
        arrow = Arrow(start=tracker_text.get_center()+LEFT*tracker_text.width/2, end=LEFT*3.2 + DOWN*0.0).set_color(PURE_BLUE)
        tracking_text = Tex(r"Tracking: finding the path or ``track'' that a particle took through the detector.", font_size=35).to_edge(DOWN, buff=1)

        self.play(FadeOut(data_pipeline_short), cms_image.animate.shift(LEFT*2.5), *[Create(o) for o in circles], Write(tracker_text), Create(arrow))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(tracking_text))
        self.next_slide(loop=True)

        n_particles = 30
        for _ in range(3):
            particles = [Dot().move_to(circle1.get_center()) for _ in range(n_particles)]
            for p in particles:
                p.move_to(circle1.get_center())
            paths = [TracedPath(p.get_center, dissipating_time=0.3, stroke_opacity=[0, 1]) for p in particles]
            self.add(*paths)
            final_angles = 2*PI*np.random.rand(n_particles)
            self.play(*[p.animate(path_arc=1.5*PI*(np.random.rand()-0.5)).shift(2.1*0.6*(RIGHT*np.cos(angle) + UP*np.sin(angle))).scale(0) for p,angle in zip(particles, final_angles)] , rate_func=linear)
            self.wait(0.3)
            self.remove(*paths)
            self.remove(*particles)

        tracker_title = Tex(r"The CMS Outer Tracker", font_size=50).shift(UP*3.5)

        self.next_slide()
        self.play(ReplacementTransform(tracker_text, tracker_title), FadeOut(cms_image), Uncreate(arrow), FadeOut(cms_detector), FadeOut(tracking_text), *[o.animate.scale(2.2).shift(4*LEFT + 0.5*UP) for o in circles])

        line = Line(start=circle1.get_center(), end=circle1.get_center()+RIGHT*0.6*2.2*2.1)
        initial_dots = [Dot().move_to(circle1.get_center()+RIGHT*0.6*2.2*d/2) for d in [1, 1.8, 2.6, 3.4, 4.2]]
        random_dots = []
        n_random_dots = 20
        np.random.seed(42)
        for d in [1, 1.8, 2.6, 3.4, 4.2]:
            angles = 2*PI*np.random.rand(n_random_dots)
            random_dots.extend([Dot().move_to(circle1.get_center()+d/2*0.6*2.2*(RIGHT*np.cos(angle) + UP*np.sin(angle))) for angle in angles])

        def track(t, dots):
            if t < 0:
                t += 1
                return (1-t)*circle1.get_center() + t*dots[0].get_center()
            n_dot = int(np.floor(t))
            t -= n_dot
            return (1-t)*dots[n_dot].get_center() + t*dots[n_dot+1].get_center()

        track1 = [19, 22, 44, 71, 90]
        track2 = [19, 22, 46, 82, 82]
        track3 = [19, 36, 46, 78, 97]
        func1 = ParametricFunction(lambda t: track(t, [random_dots[i] for i in track1]), t_range = np.array([-1, 3.99]), fill_opacity=0).set_color(ORANGE)
        func2 = ParametricFunction(lambda t: track(t, [random_dots[i] for i in track2]), t_range = np.array([-1, 3.99]), fill_opacity=0).set_color(ORANGE)
        func3 = ParametricFunction(lambda t: track(t, [random_dots[i] for i in track3]), t_range = np.array([-1, 3.99]), fill_opacity=0).set_color(ORANGE)

        self.wait(0.1)
        self.next_slide()
        self.play(Create(line))
        self.wait(0.1)
        self.next_slide()
        self.play(*[Create(o) for o in initial_dots], FadeOut(line))
        self.wait(0.1)
        self.next_slide()
        self.play(AnimationGroup(*[Create(o) for o in random_dots], lag_ratio=0.1, run_time=1))
        self.wait(0.1)
        self.next_slide()
        self.play(random_dots[19].animate.set_color(ORANGE))
        self.wait(0.1)
        self.next_slide()
        self.play(*[random_dots[o].animate.set_color(ORANGE) for o in track1[1:]], Create(func1))
        self.wait(0.1)
        self.next_slide()
        self.play(*[random_dots[o].animate.set_color(WHITE) for o in track1[1:]], Uncreate(func1))
        self.play(*[random_dots[o].animate.set_color(ORANGE) for o in track2[1:]], Create(func2))
        self.wait(0.1)
        self.next_slide()
        self.play(*[random_dots[o].animate.set_color(WHITE) for o in track2[1:]], Uncreate(func2))
        self.play(*[random_dots[o].animate.set_color(ORANGE) for o in track3[1:]], Create(func3))
        self.wait(0.1)
        self.next_slide()
        self.play(*[Uncreate(o) for o in random_dots+initial_dots+circles+[func3]], FadeOut(tracker_title))

class Scene4(Slide):

    def construct(self):

        tracking_title = Tex(r"Tracking is difficult", font_size=50).shift(UP*3.5)
        tracks_image = ImageMobject("./images/pileup_86.png").scale_to_fit_height(5).to_edge(DOWN, buff=0.3)

        blist = BulletedList(
            "Tracking accounts for $\sim$40\% of reconstruction time.",
            "Currently done on CPUs, using Klaman Filtering algorithms.",
            "At the High Luminosity LHC (HL-LHC) in $\sim$2028 the number of tracks will be so large that the computational needs will exceed the expected hardware capabilities with current algorithms.",
            font_size=35,
        ).next_to(tracking_title, DOWN, buff=0.7).to_edge(LEFT, buff=0.7)

        self.play(FadeIn(tracking_title), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(blist.submobjects[0]))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(blist.submobjects[1]))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(blist.submobjects[2]))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(tracks_image), FadeOut(blist.submobjects[0]), FadeOut(blist.submobjects[1]), blist.submobjects[2].animate.shift(UP*2))
        self.wait(0.1)
        self.next_slide()

        lst_title = Tex(r"The Line Segment Tracking Algorithm", font_size=50).shift(UP*3.5)
        self.play(ReplacementTransform(tracking_title, lst_title), FadeOut(tracks_image), FadeOut(blist.submobjects[2]))
        self.wait(0.1)
        self.next_slide()

        a1 = Arc(color=PURE_RED, radius=1.0, angle=PI/2).to_edge(LEFT, buff=0.7).to_edge(DOWN, buff=0.7)
        a2 = Arc(color=PURE_RED, radius=1.1, angle=PI/2).move_arc_center_to(a1.get_arc_center())
        arcs1 = [a1]
        arcs2 = [a2]
        for r in [1.8, 2.6, 3.4, 4.2]:
            arcs1.append(Arc(color=PURE_RED, radius=r, angle=PI/2).move_arc_center_to(a1.get_arc_center()))
            arcs2.append(Arc(color=PURE_RED, radius=r+0.1, angle=PI/2).move_arc_center_to(a2.get_arc_center()))

        steps = Tex(r"{{\item Identify Mini-Doublets (MDs).}}{{\item Link suitable MDs into Line Segments (LSs).}}{{\item Link suitable LSs intro Triplets (T3s)}}{{\item Link suitable T3s into Quituplets (T5s).}}{{\item Match objects with data from inner tracker.}}{{\item Clean up.}}", tex_environment="enumerate",
                   font_size=35).shift(RIGHT*2)

        angles1 = [30, 40, 50, 60, 70]
        angles1 = [a*np.pi/180 for a in angles1]
        angles2 = [50, 45, 40, 35, 30]
        angles2 = [a*np.pi/180 for a in angles2]
        radii = [1, 1.8, 2.6, 3.4, 4.2]
        dots1 = [Dot().set_color(WHITE).move_to(a1.get_arc_center() + (r+0.05)*(UP*np.sin(a) + RIGHT*np.cos(a))).set_z_index(10) for r,a in zip(radii, angles1)]
        dots2 = [Dot().set_color(WHITE).move_to(a1.get_arc_center() + (r+0.05)*(UP*np.sin(a) + RIGHT*np.cos(a))).set_z_index(10) for r,a in zip(radii, angles2)]
        all_dots = dots1 + dots2
        ls_links = [[0,1],[1,2],[2,3],[3,4],[5,6],[6,7],[7,8],[8,9],[0,6],[5,1],[1,7],[6,2],[2,8]]
        ls = [Line(start=all_dots[d1].get_center(), end=all_dots[d2].get_center()).set_color(WHITE) for d1,d2 in ls_links]
        t3s = [0,1,2,3,4,5,6,7,8,10,11]
        t5s = [0,1,2,3,4,5,6,7]

        self.play(Write(steps), *[Create(o) for o in arcs1])
        self.wait(0.1)
        self.next_slide()
        self.play(*[steps[i].animate.set_opacity((1 if i==0 else 0.5)) for i in range(6)])
        self.wait(0.1)
        self.next_slide()
        self.play(*[Create(o) for o in arcs2])
        self.wait(0.1)
        self.next_slide()
        self.play(AnimationGroup(*[Create(o) for o in all_dots], lag_raio=0.1))
        self.wait(0.1)
        self.next_slide()
        self.play(*[steps.submobjects[i].animate.set_opacity((1 if i==1 else 0.5)) for i in range(6)])
        self.wait(0.1)
        self.next_slide()
        self.play(AnimationGroup(*[Create(o) for o in ls], lag_raio=0.1))
        self.wait(0.1)
        self.next_slide()
        self.play(*[steps.submobjects[i].animate.set_opacity((1 if i==2 else 0.5)) for i in range(6)], *[ls[i].animate.set_color(PURE_BLUE) for i in t3s])
        self.wait(0.1)
        self.next_slide()
        self.play(*[steps.submobjects[i].animate.set_opacity((1 if i==3 else 0.5)) for i in range(6)], *[ls[i].animate.set_color(YELLOW) for i in t5s])
        self.wait(0.1)
        self.next_slide()
        self.play(*[steps.submobjects[i].animate.set_opacity((1 if i==4 else 0.5)) for i in range(6)])
        self.wait(0.1)
        self.next_slide()
        self.play(*[steps.submobjects[i].animate.set_opacity((1 if i==5 else 0.5)) for i in range(6)], *[FadeOut(ls[i]) for i in range(len(ls)) if i not in t5s])
        self.wait(0.1)
        self.next_slide()
        
        blist = BulletedList(
            "Designed from the start with parallelism in mind.",
            "Aimed at running on heterogeneous architectures, mainly on GPU.",
            "Using Alpaka library as portability layer.",
            "In mid-stages of development. Already offers similar physics performance at much lower times.",
            font_size=35,
        ).next_to(tracking_title, DOWN, buff=0.7).to_edge(LEFT, buff=0.7)
        blist.submobjects[3].shift(DOWN*1.5)
        alpaka = ImageMobject("./images/alpaka.png").scale_to_fit_height(1).next_to(blist.submobjects[2], DOWN, buff=0.5)

        self.play(ReplacementTransform(steps, blist.submobjects[0]), *[Uncreate(o) for o in all_dots+arcs1+arcs2+ls[:8]])
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(blist.submobjects[1]))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(blist.submobjects[2]), FadeIn(alpaka))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(blist.submobjects[3]))
        self.wait(0.1)
        self.next_slide()
        self.play(*[FadeOut(o) for o in [blist, alpaka, lst_title]])

class Scene5(Slide):

    def construct(self):

        title = Tex(r"What have I been doing?", font_size=50).shift(UP*3.5)

        blist = BulletedList(
            "Familiarizing myself with the code.",
            "Finding and fixing bugs.",
            "Refactoring and restructuring.",
            r"Developing a CI workflow to improve code quality and keep better track\\of performance.",
            font_size=35, buff=1,
        ).next_to(title, DOWN, buff=1).to_edge(LEFT, buff=1)

        self.play(FadeIn(title), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(blist.submobjects[0]))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(blist.submobjects[1]))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(blist.submobjects[2]))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(blist.submobjects[3]))
        self.wait(0.1)
        self.next_slide()

        title2 = Tex(r"What I'm planning to do", font_size=50).shift(UP*3.5)
        blist2 = BulletedList(
            "Improve performance and code quality.",
            "Integrate into CMSSW.",
            font_size=35, buff=1,
        ).next_to(title, DOWN, buff=1).to_edge(LEFT, buff=1)
        
        cmssw1 = ImageMobject("./images/cmssw1.png").scale_to_fit_height(1).next_to(blist2.submobjects[1], DOWN, buff=0.5).to_edge(LEFT, buff=1.3)
        cmssw2 = ImageMobject("./images/cmssw2.png").scale_to_fit_height(1).next_to(cmssw1, RIGHT, buff=0.5)

        cmssw_meme = ImageMobject("./images/cmssw_meme.jpg").scale_to_fit_height(6).to_edge(RIGHT, buff=0.7)

        self.play(ReplacementTransform(VGroup(title, blist), title2))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(blist2.submobjects[0]))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(blist2.submobjects[1]))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(cmssw1), FadeIn(cmssw2))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(cmssw_meme))
        self.wait(0.1)
        self.next_slide()

        title3 = Tex(r"Thank you!", font_size=50)

        self.play(*[FadeOut(o) for o in [cmssw1, cmssw2, cmssw_meme]], ReplacementTransform(VGroup(title2, blist2), title3))
        self.wait()

class CombinedScenes(Slide):

    def construct(self):
        slideClasses = [Scene1, Scene2, Scene3, Scene4, Scene5]
        for sc in slideClasses:
            sc.construct(self)