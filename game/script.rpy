# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define S = Character("Sen Sei")
define St = Character("Student")
define N = Character("Narrator")

init:
    $ timer_range = 0
    $ timer_jump = 0

    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0
        # This is to fade the bar in and out, and is only required once in your script

    screen countdown:
        timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
        bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.

label start:
    stop sound

    play music "<from 35 to 353>audio/bg-music.mp3" loop fadein 1.0 volume 0.1 
    # queue " "
    # play sound "" # soundfx
    
    scene asset_board with dissolve

    play sound "audio/Sensei_VO/sensei_1.mp3"
    
    scene 1 with dissolve

    S "Scientists have two ways of approaching reality."

    scene asset_bg_science_dept with dissolve

    play sound "audio/narrator_VO/narrator1.mp3"

    "Exodus Academy. The year 6069. The sophomore class of sector 420."

    scene asset_board with dissolve
    
    play sound "audio/Sensei_VO/sensei_2.mp3"

    scene 1 with dissolve

    S "Does anyone care to identify the two scientific approaches in tackling reality?"
    stop sound

    scene asset_board
    
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'topic_1'

    show screen countdown
    menu:
        "Classical and Model-Dependent":
            hide screen countdown
            play sound "audio/Sensei_VO/sensei_a10_1.mp3"

            scene 1 with dissolve

            S "That's correct!"
            jump topic_1


        "Objective and Subjective":
            hide screen countdown
            play sound "audio/Sensei_VO/sensei_a10_2.mp3"
            scene 1 with dissolve
            S "This isn't journalism."
            jump topic_1

        "Empirical and Rationalist":
            hide screen countdown
            play sound "audio/Sensei_VO/sensei_a10_3.mp3"
            scene 1 with dissolve
            S "Perhaps if you're in a philosophy course."
            jump topic_1

        "Deterministic and Probabilistic":
            hide screen countdown
            play sound "audio/Sensei_VO/sensei_a10_4.mp3"
            scene 1 with dissolve
            S "Are you taking a math course?"
            jump topic_1

# LOAD SENSEI SMILING
    

label topic_1:
    
    # scene asset_classical_vs_model-depedent with dissolve
    
    # hide sen_sei_smiling

    play sound "audio/Sensei_VO/sensei_3.mp3"
    scene 1 with dissolve
    S "Today, we'll be discussing classical and model-dependent realism."
    stop sound

    play sound "audio/narrator_VO/Narrator2.mp3"
    St "Classical and model-dependent realism?"
    stop sound

    play sound "audio/Sensei_VO/sensei_4.mp3"
    S "That's right. Classical realism claims that there's an objective reality independent of our observations and theories."
    stop sound

    play sound "audio/narrator_VO/Narrator3.mp3"
    St "That must mean that there's a singular truth. A true description of reality."
    stop sound
    
    play sound "audio/Sensei_VO/sensei_5.mp3"
    
    S "In classical realism, we scientists craft theories to accurately describe the truth of reality."
    stop sound

    scene 2 with dissolve

    play sound "audio/narrator_VO/Narrator4.mp3"
    N "Sen Sei paces around the board."
    
    stop sound

    scene 32 with dissolve
    play sound "audio/Sensei_VO/sensei_6.mp3"
    S "The second approach is model-dependent realism. What does that mean?"
    stop sound

    play sound "audio/narrator_VO/Narrator5.mp3"
    St "It means that reality depends on multiple models?"
    stop sound

    play sound "<from 0 to 15>audio/Sensei_VO/sensei_7.mp3"
    S "Well, in model-dependent realism, our grasp of reality is limited by our models and theories. Reality is understood through various models. These models may offer differing descriptions of reality."
    stop sound

    play sound "<from 15.3 to 23.5>audio/Sensei_VO/sensei_7.mp3"
    S "A single theory may not capture what reality is. It's quite a philosophical approach to science."
    stop sound

    # LOAD SENSEI NEUTRAL
    scene 3 with dissolve

    play sound "audio/narrator_VO/Narrator6.mp3"
    N "Sen Sei stops and takes out a tablet."
    stop sound

    scene 4 with dissolve

    play sound "audio/Sensei_VO/sensei_8.mp3"

    S "Now it's time for a fun activity. You were placed into groups, right? Are you ready for a group quiz?"
    stop sound

    play sound "audio/narrator_VO/Narrator7.mp3"
    N "An innocent sentence flashes on the board."
    stop sound

    play sound "audio/Sensei_VO/sensei_9.mp3"
    S "You are to write your answers on a piece of paper. Once the timer reaches zero, your group will show us your answer."
    stop sound

    play sound "audio/narrator_VO/Narrator8.mp3"
    N "Are you ready?"
    stop sound


    play sound "audio/Question_VO/Question1.mp3"
    S "Question 1: Model-dependent realism asserts that theories cannot capture the truth of reality."
    stop sound

    scene asset_board with dissolve

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'quiz1_q1'
    show screen countdown

    menu:
        "True":
            hide screen countdown
            pass
        
        "False":
            hide screen countdown
            pass
        
        "It depends...":
            hide screen countdown
            pass

label quiz1_q1:

    play sound "<from 0 to 12>audio/Sensei_VO/sensei_10.mp3"

    scene 5 with dissolve

    S "The correct answer is False. In model-dependent realism, theories may capture the truth of reality, but only in their respective domains. "
    stop sound

    play sound "<from 12 to 29.5>audio/Sensei_VO/sensei_10.mp3"
    S "For instance, in model-dependent realism, Newtonian physics accurately describes motion under gravity in everyday scenarios, while Einstein's general relativity offers a more precise description in extreme conditions like near black holes."
    stop sound

    scene 4 with dissolve

    play sound "audio/Question_VO/Question2.mp3"
    S "Question 2: Classical realism seeks to discover the existence or non-existence of ghosts."
    stop sound

    scene asset_board with dissolve

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'quiz1_q2'
    show screen countdown

    menu:
        "True":
            hide screen countdown
            pass
        
        "False":
            hide screen countdown
            pass

label quiz1_q2:
    scene 6 with dissolve
    play sound "<from 0 to 14>audio/Sensei_VO/sensei_11.mp3"
    S "The correct answer is True. Classical realism seeks to understand the existence or non-existence of phenomena based on an objective reality independent of human perception. "
    stop sound

    play sound "<from 14 to 29.5>audio/Sensei_VO/sensei_11.mp3"
    S "In the case of ghosts, classical realists would approach the question by investigating empirical evidence and logical reasoning to determine whether such entities exist within the framework of objective reality."
    stop sound
    
    scene 4 with dissolve
    play sound "audio/Question_VO/Question3.mp3"
    S "Question 3: In model-dependent realism, which came first: reality or the model?"
    stop sound

    scene asset_board with dissolve

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'quiz1_q3'
    show screen countdown

    menu:
        "Reality":
            hide screen countdown
            pass
        
        "Model":
            hide screen countdown
            pass
        
        "They came to be at the same time.":
            hide screen countdown
            pass

label quiz1_q3:
    scene 7 with dissolve
    play sound "<from 0 to 13>audio/Sensei_VO/sensei_12.mp3"
    S "The correct answer is that the model comes first. In model-dependent realism, our reality is shaped by the conceptual models or theories we create to interpret our observations and experiences. "
    stop sound

    play sound "<from 13 to 25.5>audio/Sensei_VO/sensei_12.mp3"
    S "These models serve as frameworks through which we perceive and make sense of reality, implying that the model precedes our understanding of what is real and what is not."
    stop sound

    scene 4 with dissolve
    play sound "audio/Question_VO/Question4.mp3"
    S "Question 4: Model-dependent realism asserts that theories cannot capture the truth of reality. Classical realism asserts that there exists a truth behind reality."
    stop sound

    scene asset_board with dissolve

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'quiz1_q4'
    show screen countdown

    menu:
        "True":
            hide screen countdown
            pass
        
        "False":
            hide screen countdown
            pass
        
        "It depends...":
            hide screen countdown
            pass

label quiz1_q4:
    scene 6 with dissolve

    play sound "<from 0 to 14>audio/Sensei_VO/sensei_13.mp3"
    # <from 5 to 15.5>
    S "The correct answer is true. In model-dependent realism, truth may be relative and context-dependent, influenced by the conceptual models or theories we use to interpret reality. "
    stop sound

    play sound "<from 14.5 to 26.5>audio/Sensei_VO/sensei_13.mp3"
    S "However, within each model, there exists a notion of truth that corresponds to the accuracy of that model in describing and predicting phenomena within its domain."
    stop sound

    scene 4 with dissolve
    play sound "audio/Question_VO/Question5.mp3"
    S "Question 5: In model-dependent realism, truth is an absolute concept."
    stop sound

    scene asset_board with dissolve

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'quiz1_q5'
    show screen countdown

    menu:
        "True":
            hide screen countdown
            pass
        
        "False":
            hide screen countdown
            pass
        
        "It depends...":
            hide screen countdown
            pass

label quiz1_q5:

    scene 8 with dissolve

    play sound "<from 0 to 17>audio/Sensei_VO/sensei_14.mp3"
    S "It depends. As in, it depends on the context and the framework of the model. In model-dependent realism, truth is not always absolute. Instead, it depends on the context and the framework within which it is interpreted. "
    stop sound

    play sound "<from 17.5 to 28>audio/Sensei_VO/sensei_14.mp3"
    S "While some models may provide a more absolute conception of truth within their specific domain, others may allow for more relative interpretations. "
    stop sound

    play sound "<from 28.5 to 39.5>audio/Sensei_VO/sensei_14.mp3"
    S "Therefore, whether truth is absolute or relative in model-dependent realism varies based on the particular model being considered and the context in which it is applied."
    stop sound

    scene 3 with dissolve
    play sound "audio/narrator_VO/Narrator9.mp3"
    "Counting the scores... Not too shabby."
    stop sound

label topic_2:
    play sound "audio/Sensei_VO/sensei_15.mp3"
    S "I see that some of you aren't paying attention. From this point forward, hold on to your paper. I will be asking questions that will be answered as a group, timed, and graded accordingly. Let's move on to the story of a very interesting man and how he determined that the universe is expanding."
    stop sound

    # LOAD EDWIN HUBBLE
    scene 10 with dissolve

    play sound "audio/narrator_VO/Narrator10.mp3"
    N "Edwin Hubble. A 20th century American scientist who played a crucial role in establishing extragalctic astronomy and observational cosmology."
    stop sound

    # LOAD SENSEI SMILING

    play sound "audio/Sensei_VO/sensei_16.mp3"
    S "Edwin Hubble was a pioneer of the stars. He fed his curiosity through science fiction novels."
    stop sound

    play sound "audio/narrator_VO/Narrator11.mp3"
    St "How strange that his fiction of yesterday is the reality of tomorrow."
    stop sound

    # LOAD SENSEI NEUTRAL

    play sound "audio/Sensei_VO/sensei_17.mp3"
    S "In the twentieth century, ages ago, Edwin Hubble set his sights on the heavens. He used the 100-inch Hooker Telescope, the world’s largest at the time, to observe faint, fuzzy, cloud-like patches of light in the cosmos. What are these patches of light called?"
    stop sound

    scene 33 with dissolve
    
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'quiz2_q1'
    show screen countdown

    menu:
        "Stars":
            
            hide screen countdown
            pass
        
        "Supernovas":
            hide screen countdown
            pass
        
        "Galaxies":
            hide screen countdown
            pass

        "Nebula":
            hide screen countdown
            play sound "audio/Sensei_VO/sensei_a10_1.mp3"

            # scene 1 with dissolve

            S "That's correct!"
            jump quiz2_q1
            # pass

        "Quasars":
            hide screen countdown
            pass

label quiz2_q1:

    scene 10 with dissolve

    play sound "audio/Sensei_VO/sensei_18.mp3"
    S "These patches of light were nebula. Nebulae. Up until the early 20th century, our perception of the cosmos fell within the boundaries of the Milky Way. There were speculations of other galaxies. However, it wasn't until Hubble turned his telescope on Andromeda that our perception would change."
    stop sound

    # LOAD ANDROMEDA
    scene asset_andromeda with dissolve
    show c1 at right:
        xzoom 1.7 yzoom 1.7
        align((1.4, 0.6))
    play sound "audio/narrator_VO/Narrator12.mp3"
    S "The Andromeda galaxy. Our nearest galactical neighbor."
    stop sound

    
    play sound "audio/Sensei_VO/sensei_19.mp3"
    S "Back then, Andromeda was believed to be a nebula. Hubble studied the light emitted from Andromeda and concluded that Andromeda was a galaxy as well. He used this technique to discover other galaxies."
    stop sound

    play sound "audio/narrator_VO/Narrator13.mp3"
    St "The Doppler Effect applied to light, aptly named redshift. Light from a distance appears displaced towards the red end of the spectrum."
    stop sound
    
    play sound "audio/Sensei_VO/sensei_20.mp3"
    S "The redshift of light from distant galaxies indicates that they're moving away from us. The greater the redshift, the faster the galaxies are moving away. This led to the conception of Hubble's Law. Can anyone guess what Hubble's Law states?"
    stop sound

    scene 33 with dissolve

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'quiz2_q2'
    show screen countdown

    menu:
        "The size of a galaxy is directly proportional to its distance from us.":
            hide screen countdown
            pass
        
        "The brightness of a galaxy is directly proportional to its distance from us.":
            hide screen countdown
            pass
        
        "The age of a galaxy is directly proportional to its distance from us.":
            hide screen countdown
            pass

        "The velocity of a galaxy is directly proportional to its distance from us.":
            hide screen countdown

            play sound "audio/Sensei_VO/sensei_a10_1.mp3"
            S "That's correct!"
            jump quiz2_q2

            pass

label quiz2_q2:

    scene 10 with dissolve

    play sound "audio/Sensei_VO/sensei_21.mp3"
    S "Hubble's Law states that the velocity of a galaxy is directly proportional to its distance from us. This observation provided compelling evidence for the expansion of the universe. Hubble's Law also implies that the universe expands uniformly across all directions."
    stop sound
    
    scene 11 with dissolve

    play sound "audio/narrator_VO/Narrator14.mp3"
    N "A single innocuous question appears on the board."
    stop sound
    
    play sound "audio/Question_VO/Question6.mp3"
    S "Question: Does Edwin Hubble's study of the cosmos align with model-dependent realism or classical realism?"
    stop sound

    scene 33 with dissolve

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'quiz2_q3'
    show screen countdown

    menu:
        "Model-dependent realism.":
            hide screen countdown
            pass
        
        "Classical realism.":
            hide screen countdown
            play sound "audio/Sensei_VO/sensei_a10_1.mp3"
            S "That's correct!"
            jump quiz2_q3
            
        
        "Neither, Edwin Hubble's study was aligned with subjectivism.":
            hide screen countdown
            pass

        "It was aligned with both.":
            hide screen countdown
            pass

        "None of the above.":
            hide screen countdown
            pass

label quiz2_q3:
    scene 12 with dissolve

    play sound "<from 0 to 23>audio/Sensei_VO/sensei_22.mp3"
    S "The answer is classical realism. Edwin Hubble's study of the cosmos aligns more closely with classical realism. His work was grounded in empirical observation and aimed to uncover an objective truth about the universe, consistent with the principles of classical realism. "
    stop sound
    
    play sound "<from 23.5 to 39.5>audio/Sensei_VO/sensei_22.mp3"
    S "Hubble's observations, such as the discovery of the expanding universe and the formulation of Hubble's Law, contributed to our understanding of the cosmos as an objective reality governed by natural laws."
    stop sound

label topic_3:
    # LOAD SENSEI NEUTRAL

    play sound "audio/Sensei_VO/sensei_23.mp3"
    S "This leads us to our next topic of discussion. How did the universe come about, anyway?"
    stop sound

    scene 14 with dissolve

    play sound "audio/narrator_VO/Narrator15.mp3"
    "The Big Bang. That's something that everyone knows."
    stop sound

    play sound "audio/Sensei_VO/sensei_24.mp3"
    S "About 14 billions years ago, the Big Bang occured. Despite the name, the Big Bang wasn't a violent explosion. Instead, it was the rapid expansion of a very hot and very dense universe, filled with quarks, gluons, and other elementary particles."
    stop sound

    play sound "audio/narrator_VO/Narrator16.mp3"
    "So it didn't explode like a bomb."
    stop sound

    play sound "audio/Sensei_VO/sensei_25.mp3"
    S "As the universe expanded and cooled, quarks merged together to form protons and neutrons, which then combined to form atomic nuclei, such as hydrogen and helium. This occured about a hundred seconds after the Big Bang. What do you think is the name of this phenomena?"
    stop sound
    
    scene 34 with dissolve

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'quiz2_q4'
    show screen countdown

    menu:
        "Big Bang Fusion.":
            hide screen countdown
            pass
        
        "Primordial Genesis":
            hide screen countdown
            pass
        
        "Big Bang Nucleation.":
            hide screen countdown
            pass

        "Big Bang Nucleosynthesis":
            hide screen countdown
            pass       

        "None of the above.":
            hide screen countdown
            pass


label quiz2_q4:
    scene 15 with dissolve
    play sound "audio/Sensei_VO/sensei_26.mp3"
    S "Hmmm. This phenomena is called Big Bang Nucleosynthesis, during which light elements like hydrogen and helium were formed from the fusion of protons and neutrons in the early universe."
    stop sound

    play sound "audio/narrator_VO/Narrator17.mp3"
    "The early universe, the primordial soup, from which our universe came to be."
    stop sound

    play sound "audio/Sensei_VO/sensei_27.mp3"
    S "The universe continued to expand and cool, and electrons combined with atomic nuclei to form neutral atoms, 380,000 years after the Big Bang. This process was called..."
    stop sound

    scene 34 with dissolve

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'quiz2_q5'
    show screen countdown

    menu:
        "Nucleosynthesis":
            hide screen countdown
            pass
        
        "Genesis":
            hide screen countdown
            pass
        
        "Atomization":
            hide screen countdown
            pass

        "Recombination":
            hide screen countdown
            play sound "audio/Sensei_VO/sensei_a10_1.mp3"
            S "That's correct!"
            jump quiz2_q5

        "Coalescense":
            hide screen countdown
            pass

        "None of the above.":
            hide screen countdown
            pass

label quiz2_q5:

    scene 16 with dissolve

    play sound "audio/Sensei_VO/sensei_28.mp3"
    S "It's called recombination. After neutral atoms were formed through recombination, the universe still continued to expand and cool. Stars and galaxies formed from the gravitational collapse of clouds of dust and gas. "
    stop sound

    S "And then came our planets"

    play sound "audio/Sensei_VO/sensei_29.mp3"
    S "Where do you think did the later, life-supporting elements such as carbon, nitrogen, and oxygen originate from?"
    stop sound
    
    scene 34 with dissolve

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'quiz2_q6'

    show screen countdown
    menu:
        "Stars":
            hide screen countdown
            play sound "audio/Sensei_VO/sensei_a10_1.mp3"
            S "That's correct!"
            jump quiz2_q6
        
        "Suns":
            hide screen countdown
            pass
        
        "Planetary Cores":
            hide screen countdown
            pass

        "Dwarf Planets":
            hide screen countdown
            pass

        "Galaxies":
            hide screen countdown
            pass

        "Dead Planets":
            hide screen countdown
            pass


label quiz2_q6:
    scene 18 with dissolve

    play sound "<from 0 to 14>audio/Sensei_VO/sensei_30.mp3"
    S "Stars manufactured these elements. Life-supporting elements such as carbon, nitrogen, and oxygen primarily originate from the nuclear fusion processes that occur within stars. "
    stop sound

    scene 19 with dissolve

    play sound "<from 14.3 to 26.5>audio/Sensei_VO/sensei_30.mp3"
    S "During the later stages of stellar evolution, massive stars undergo nucleosynthesis, where heavier elements are formed through fusion reactions in their cores."
    stop sound

    scene 20 with dissolve

    play sound "<from 27 to 39>audio/Sensei_VO/sensei_30.mp3"
    S "When these stars eventually explode in supernova events, they release these elements into space, enriching the interstellar medium with the building blocks of life."
    stop sound

    scene 21 with dissolve

    play sound "<from 39.5 to 48.5>audio/Sensei_VO/sensei_30.mp3"
    S "Subsequently, these elements are incorporated into new generations of stars, planets, and ultimately, life forms."
    stop sound

    scene 22 with dissolve
    play sound "audio/narrator_VO/Narrator18.mp3"
    "Did humans come from space?"
    stop sound

    # LOAD SENSEI SMILING

label topic_4:

    play sound "audio/Sensei_VO/sensei_31.mp3"
    S "Now, we have our last topic for the day. We'll be tracing the evolution of a high-mass star."
    stop sound
    
    # LOAD ASSET STAR1
    scene 23 with dissolve

    play sound "audio/Sensei_VO/sensei_32.mp3"
    S "A high-mass star starts its life as a main sequence star, burning hydrogen into helium in its core. You may think of stars as a nuclear powerplant, where nuclear fusion reigns supreme."
    stop sound
    
    # LOAD ASSET STAR2
    scene 24 with dissolve

    play sound "audio/Sensei_VO/sensei_33.mp3"
    S "As the star exhausts its hydrogen fuel, it expands and becomes a red supergiant."
    stop sound

    # LOAD ASSET STAR3
    scene 25 with dissolve

    play sound "audio/Sensei_VO/sensei_34.mp3"
    S "The core of the star contracts and heats up, and it starts burning helium into carbon and oxygen."
    stop sound
    
    # LOAD ASSET STAR4
    scene 26 with dissolve

    play sound "audio/Sensei_VO/sensei_35.mp3"
    S "The outer layers of the star expand and cool, and the star becomes larger and brighter."
    stop sound

    # LOAD ASSET STAR5
    scene 27 with dissolve

    play sound "audio/Sensei_VO/sensei_36.mp3"
    S "The core of the star continues to contract and heat up, and it starts burning heavier elements, such as carbon, oxygen, and so on."
    stop sound

    # LOAD ASSET STAR6
    scene 28 with dissolve

    play sound "audio/Sensei_VO/sensei_37.mp3"
    S "Eventually, the core of the star becomes so hot and dense that it forms a degenerate iron core."
    stop sound

    # LOAD ASSET STAR7
    scene 29 with dissolve

    play sound "audio/Sensei_VO/sensei_38.mp3"
    S "The iron core is unable to sustain nuclear fusion, and it collapses under its own gravity, leading to a supernova explosion."
    stop sound

    # LOAD ASSET STAR8
    scene 30 with dissolve

    play sound "audio/Sensei_VO/sensei_39.mp3"
    S "The supernova explosion scatters the outer layers of the star into space, and it forms a neutron star or a black hole, depending on the mass of the core."
    stop sound
    
    # LOAD SENSEI NEUTRAL
    
    scene 31 with dissolve

    play sound "audio/Sensei_VO/sensei_40.mp3"
    S "I hope you learned something from today's discussion."
    stop sound
    

    # LOAD SENSEI SMILING
    
    play sound "audio/Sensei_VO/sensei_41.mp3"
    S "Oh, and for the group that got the most points, please claim your reward up front."
    stop sound

    # LOAD ASSET_END

return
