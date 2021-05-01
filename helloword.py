from manim import *
from numpy import *

class VectorArrow(Scene):
    def construct(self):

        delta = ValueTracker(0)
        self.sumReal = 0 
        self.sumImag = 0 
        self.j = 0 
        vectorsToAnimate = [ Arrow([0,0,0],[1,1,0]), Arrow([0,0,0], [2,2,0]) ]
        transformationsToPlay = []

        for vector in vectorsToAnimate:
            transformationsToPlay.appned(self.updateVector(vector))

        self.play(*transformationsToPlay)

    def updateVector(self, vectorToUpdate):

        endPointOfPrevVector = np.cfloat(self.sumReal)
        updatedStartingPoint = [np.imag(endPointOfPrevVector), np.real(endPointOfPrevVector), 0]

        def calculateNewVector():
            # diff = np.cfloat(1) / np.cfloat(resolution) * np.exp ^ ( 2 * np.pi * ( j * delta.get_value() ) ) * vectorToUpdate
            # imag = np.imag(diff)
            # real = np.real(diff)
            return [self.sumReal + self.j, self.sumImag + self.j , 0]

        updatedVector = Arrow(updatedStartingPoint, calculateNewVector() )
        transformation = Transform(vectorToUpdate, updatedVector)
        self.sumReal += 1
        self.sumImag += 1
        self.j += 1

        return transformation


        
        



    
       

# rotation_center = LEFT

#         theta_tracker = ValueTracker(110)
#         line1 = Line(LEFT, RIGHT)
#         line_moving = Line(LEFT, RIGHT)
#         line_ref = line_moving.copy()
#         line_moving.rotate(
#             theta_tracker.get_value() * DEGREES, about_point=rotation_center
#         )
#         a = Angle(line1, line_moving, radius=0.5, other_angle=False)
#         te = MathTex(r"\theta").move_to(
#             Angle(
#                 line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
#             ).point_from_proportion(0.5)
#         )

#         self.add(line1, line_moving, a, te)
#         self.wait()

#         line_moving.add_updater(
#             lambda x: x.become(line_ref.copy()).rotate(
#                 theta_tracker.get_value() * DEGREES, about_point=rotation_center
#             )
#         )

#         a.add_updater(
#             lambda x: x.become(Angle(line1, line_moving, radius=0.5, other_angle=False))
#         )
#         te.add_updater(
#             lambda x: x.move_to(
#                 Angle(
#                     line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
#                 ).point_from_proportion(0.5)
#             )
#         )

#         self.play(theta_tracker.animate.set_value(40))
#         self.play(theta_tracker.animate.increment_value(140))
#         self.play(te.animate.set_color(RED), run_time=0.5)
#         self.play(theta_tracker.animate.set_value(350))
        