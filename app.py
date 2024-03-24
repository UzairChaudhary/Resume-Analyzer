from flask import Flask, render_template, url_for, request, session, redirect, abort, jsonify
from werkzeug.utils import secure_filename
import spacy, fitz
from ResumeAnalysis.utility.downloadFile import download_file
from ResumeAnalysis.utility.extractTextFromPdf import extractTextFromPdf
from ResumeAnalysis.calculateSimilarity import calculate_similarity


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'


download_folder = 'ResumeAnalysis/Downloads'  # Update this to the desired folder path

# API endpoint for calculating similarity
@app.route('/api/calculate_similarity', methods=['POST'])
def api_calculate_similarity():
    try:
        data = request.json
        print(data)
        # Extract resume and job description URLs from the request data
        resume_url = data.get('resumeUrl')
        job_description_url = data.get('jobDescriptionUrl')
        # Download Resume File from URL
        resume_file = download_file(resume_url, download_folder)
        #doc = fitz.open(resume_file)
        # print("-----------------Resume----------------")
        # #print(doc)
        # print("Resume taken as input")
        # # Load the spacy model
        # print("Loading Resume Parser model...")
        # resume_nlp = spacy.load('ResumeAnalysis/assets/ResumeModel/output/model-best')
        # print("Resume Parser Model Loaded")
        # resume_dic = extractTextFromPdf(doc, resume_nlp)
        # print("Resume Parser Model work done")
        # # Resume Dictionary
        # print("---------Resume Dictionary-----------")
        # print(resume_dic)
        
        # doc.close()
        
        # job_description_file = download_file(job_description_url, download_folder)
        # jd_doc = fitz.open(job_description_file)
        # # Spacy model for Job Description
        
        # print("Loading Jd Parser model...")
        # jd_nlp = spacy.load('ResumeAnalysis/assets/JdModel/output/model-best')
        # print("Jd Parser model loaded")
        # jd_dic = extractTextFromPdf(jd_doc, jd_nlp)
        # print("JD Parser Model work done")
        # # Job Description Dictionary
        # print("---------JD Dictionary-----------")
        # print(jd_dic)
        
        # jd_doc.close()
        
        
        
        
        with fitz.open(resume_file) as doc:
            print("Resume taken as input")
            # Load the spacy model
            print("Loading Resume Parser model...")
            resume_nlp = spacy.load('ResumeAnalysis/assets/ResumeModel/output/model-best')
            print("Resume Parser Model Loaded")
            resume_dic = extractTextFromPdf(doc, resume_nlp)
            print("Resume Parser Model work done")
            # Resume Dictionary
            print(resume_dic)

        # Download job description file from URL
        job_description_file = download_file(job_description_url, download_folder)
        with fitz.open(job_description_file) as jd_doc:
            # Spacy model for Job Description
            print("Loading Jd Parser model...")
            jd_nlp = spacy.load('ResumeAnalysis/assets/JdModel/output/model-best')
            print("Jd Parser model loaded")
            jd_dic = extractTextFromPdf(jd_doc, jd_nlp)
            print("JD Parser Model work done")
            # Job Description Dictionary
            print(jd_dic)
        
        similarity_percentage = calculate_similarity(resume_dic, jd_dic)

          
        
        return jsonify({'similarity_percentage': similarity_percentage})
        

    except Exception as e:
        print(e)
        return jsonify({'error': 'Internal Server Error'}), 500
    


if __name__ == '__main__':
    app.run(debug=True)
