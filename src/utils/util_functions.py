import os
import streamlit as st 
import pandas as pd
from src.generator.question_generator import QuestionGenerator

# reset
def rerun():
    st.session_state['rerun_trigger'] = not st.session_state.get('rerun_trigger', False )

class QuizManager:
    def __init__(self):
        self.questions=[]
        self.user_answers=[]
        self.results=[]    
    
    def generate_question(self,generator :QuestionGenerator,topic:str,question_type:str,difficulty:str,num_questions:int):
        self.questions=[]
        self.user_answers=[]
        self.results=[]
        
        try:
            for _ in range(num_questions):
                if question_type == "Multiple Choice":
                    question=generator.generate_mcq(topic,difficulty.lower())
                    
                    self.questions.append({
                        'type': 'MCQ',
                        'question': question.question,
                        'options': question.options,
                        'correct_answer': question.correct_answer})
                else:
                    question=generator.generate_fill_blank(topic,difficulty.lower())
                    self.questions.append({
                        'type': 'Fill in the Blank',
                        'question': question.question,
                        'correct_answer': question.correct_answer})    
    
        except Exception as e:
            st.error(f"Error generating question {e}")
            return False
        
        return True    
    
    def attempt_quiz(self):
        for i,q in enumerate(self.questions):
            st.markdown(f"**Question {i+1} : {q['question']}**")
            
            if q['type']=='MCQ':
                #store user answer
                user_answer = st.radio(
                    f"Select and answer for Question {i+1}",
                    q['options'],
                    key=f"mcq_{i}"
                )
                self.user_answers.append(user_answer)
            else:
                user_answer=st.text_input(
                    f"Fill in the blank for Question {i+1}",
                    key = f"fill_blank_{i}"
                )

                self.user_answers.append(user_answer)        