from manimlib.imports import *
import os
import pyclbr

class DiscreteCompounding(Scene):
    #A short script showing how to use Latex commands
    def construct(self):
        compound_interest = TexMobject("A = P(1+r)^{t}")
        compound_interest.shift(2*UP)

        msg1 = TextMobject("Let's Consider for semi-annual ...")
        msg2 = TextMobject("now r = r/2 each for semesters")
        msg3 = TextMobject("t = t(years) * 2")
        msg1.shift(2*UP)
        msg2.shift(2*UP)
        msg3.shift(2*UP)

        semiannual_interest = TexMobject("A = P(1+r/2)^{t*2}")
        semiannual_interest.shift(UP)

        msg4 = TextMobject("Generalising for n periods")
        msg4.shift(2*UP)

        general_compound_interest = TexMobject("A = P(1+r/n)^{t*n}")
 
        self.play(Write(compound_interest))
        self.wait(2)
        self.play(FadeOut(compound_interest))
        self.wait(1)
        self.play(Write(msg1))
        self.wait(2)
        self.play(FadeOut(msg1))
        self.wait(1)
        self.play(Write(msg2))
        self.wait(2)
        self.play(FadeOut(msg2))
        self.wait(1)
        self.play(Write(msg3))
        self.wait(2)
        self.play(FadeOut(msg3))
        self.wait(1)
        self.play(Write(semiannual_interest))
        self.wait(3)
        self.play(FadeOut(semiannual_interest))
        self.wait(1)
        self.play(Write(msg4))
        self.wait(2)
        self.wait(1)
        self.play(Write(general_compound_interest))
        self.play(FadeOut(msg4))
        self.wait(3)
        self.play(FadeOut(general_compound_interest))

class ContinuousCompounding(Scene):
    #A short script showing how to use Latex commands
    def construct(self):
        msg1 = TextMobject("Consider the following limit(Remember this !!!) ")
        msg1.shift(UP)

        limit_equation = TexMobject("\lim_{x\to\infty} (1 + 1/x)^{x} = e")
        general_compound_interest = TexMobject("A = P(1+r/n)^{t*n}")

        msg2 = TextMobject("As a limiting case if n is very large (theoretical)")
        msg2.shift(UP)

        limiting_general_compound_interest = TexMobject("\lim_{n\to\infty} P(1+r/n)^{t*n}")
        limiting_general_compound_interest.shift(UP)

        msg3 = TextMobject("replacing n/r with x")
        
        modified_equation_1 = TexMobject("\lim_{x\to\infty} P(1+1/x)^{x * r * t}")
        modified_equation_2 = TexMobject("P (\lim_{x\to\infty} ((1+1/x)^{x}))^{r*t}")

        final_equation = TexMobject("A = Pe^{r*t}")



        self.play(Write(msg1))
        self.play(Write(limit_equation))
        self.wait(3)
        self.play(FadeOut(msg1))
        self.play(FadeOut(limit_equation))
        self.play(Write(general_compound_interest))
        self.play(Write(msg2))
        self.wait(2)
        self.play(FadeOut(msg2))
        self.play(FadeOut(general_compound_interest))
        self.play(Write(limiting_general_compound_interest))
        self.wait(3)
        self.play(Write(msg3))
        self.wait(2)
        self.play(FadeOut(msg3))
        self.play(FadeOut(limiting_general_compound_interest))
        self.play(Write(modified_equation_1))
        self.wait(3)
        self.play(FadeOut(modified_equation_1))
        self.play(Write(modified_equation_2))
        self.wait(3)
        self.play(FadeOut(modified_equation_2))
        self.play(Write(final_equation))

class ZeroIncome(Scene):
    #A short script showing how to use Latex commands
    def construct(self):
        msg1 = TextMobject("Spot Price $S_0$")
        msg2 = TextMobject("Forward Price $F_0$")
        msg3 = TextMobject("Risk Free Rate r")
        msg1.shift(UP*2)
        msg2.shift(UP*1.5)
        msg3.shift(UP*1)

        msg4 = TextMobject("If you think Forward price is higher")
        msg5 = TextMobject("Borrow $S_0$, this would become $S_0e^{rt}$ after t years")
        msg6 = TextMobject("Buy the stock @ $S_0$")
        msg7 = TextMobject("For zero arbitrage")

        msg4.shift(UP*2.5)
        msg5.shift(UP*2)
        msg6.shift(UP*1.5)
        
        equation = TexMobject("F_0 - S_0e^{rt} = 0")
        final_equation = TexMobject("F_0 = S_0e^{rt}")

        equation.shift(UP*1)
        msg7.shift(UP*0.5)


        self.play(Write(msg1))
        self.play(Write(msg2))
        self.play(Write(msg3))
        self.wait(2)
        self.play(FadeOut(msg1))
        self.play(FadeOut(msg2))
        self.play(FadeOut(msg3))
        self.play(Write(msg4))
        self.play(Write(msg5))
        self.play(Write(msg6))
        
        self.play(Write(equation))
        self.play(Write(msg7))
        self.play(Write(final_equation))
        self.wait(3)
        self.play(FadeOut(msg4))
        self.play(FadeOut(msg5))
        self.play(FadeOut(msg6))
        self.play(FadeOut(equation))
        self.play(FadeOut(msg7))   
        

if __name__ == "__main__":
    # Call this file at command line to make sure all scenes work with version of manim
    # type "python manim_tutorial_P37.py" at command line to run all scenes in this file
    #Must have "import os" and  "import pyclbr" at start of file to use this
    ###Using Python class browser to determine which classes are defined in this file
    module_name = 'manim_tutorial_P37'   #Name of current file
    module_info = pyclbr.readmodule(module_name)

    for item in module_info.values():
        if item.module==module_name:
            print(item.name)
            os.system("python -m manim manim_tutorial_P37.py %s -l" % item.name)  #Does not play files


