# Topics:

- What is NLP?
- Real World Applications of NLP.
- Common NLP Tasks
- Approaches in NLP
- NLP Pipeline 
- 
<br>

# `#01 What is NLP:`

<br>
Natural language processing is a subfield of linguistics,computer science and artificial intelligence concerned with the interactions between computers and human language, inparticular how to progrma computer to process and analyze large amounts of natural language data.

<br>

# `#02 Real World Applicaitons:`

<br>
- Contextual Advertisements
- Email Clients - spam filtering,smart reply
- Social Media - removing adult content, opinion mining
- Search Engines
- Chatbots


<br>

# `#03 Common NLP Tasks:`

<br>

- Text/Document Classification
- Sentiment Analysis
- Information Retrieval **(RAG type application)**.
- Parts of Speech Tagging **(find noun,verb,adjective)**.
- Machine Translation or language translation
- Conversational Agents
- Knowledge Graph **(use in google search)**
- Text summarization
- Text generation or next word predictor
- Speech to Text

<br>

# `#04 Approaches in NLP:`

<br>

- **1. Heuristic Method.**
- **2. Machine learning Based.**
- **3. Deep learning Based.**
<br>

## **1. Heuristic Method: (Rule-Based Approach)**  
### **বৈশিষ্ট্য:**  
- ভাষার ব্যাকরণ, নিয়ম (রুলস) এবং অভিধান ব্যবহার করে তৈরি করা হতো।  
- প্রোগ্রামার বা ভাষাবিদদের দ্বারা ম্যানুয়ালি নিয়ম ডিজাইন করতে হতো।  
### **Era:**  
১৯৬০–১৯৯০ সাল পর্যন্ত (মেশিন লার্নিং আসার আগে)।  
### **উদাহরণ:**  
- **ELIZA (১৯৬৬):** প্রথম চ্যাটবট, সাইকোথেরাপি সিমুলেট করত (যেমন: "Tell me more about your family")।  
- **গ্রামার চেকার:** "He go to school" → "go" কে "goes" করতে বলত (ব্যাকরণ রুল ম্যাচ করে)।  
- **স্ট্রিং ম্যাচিং:** যেমন, "ঢাকা থেকে চট্টগ্রাম যাওয়ার বাস?" → "ঢাকা" এবং "চট্টগ্রাম" শব্দ ম্যাচ করে উত্তর দেয়া।  
### **সীমাবদ্ধতা:**  
- নতুন বাক্য বা শব্দ এলেই কাজ করত না।  
- প্রতিটি ভাষার জন্য আলাদা নিয়ম বানাতে হতো।  


## **2. Machine learning Based:(Statistical Approach)**  
### **বৈশিষ্ট্য:**  
-  Uses statistical models trained on data (e.g., Naïve Bayes, SVM, HMMs) for tasks like classification or sequence labeling.
- **Feature Engineering:** প্রয়োজন হতো (যেমন: শব্দের পজিশন, পার্ট-অফ-স্পিচ)।  
### **Era:** ১৯৯০–২০১০ সাল (ডিপ লার্নিং আসার আগে)।  
### **উদাহরণ:**  
- **Statistical Machine Translation (SMT):**  
  - গুগল ট্রান্সলেট (২০০৬–২০১৬) "Phrase-Based SMT" ব্যবহার করত।  
  - বাংলা → ইংরেজি অনুবাদে শব্দের সম্ভাব্যতা (Probability) হিসাব করত।  
- **স্প্যাম ফিল্টার:** Naïve Bayes অ্যালগরিদম ব্যবহার করে ইমেইল ক্লাসিফাই করা।  
- **পার্ট-অফ-স্পিচ ট্যাগিং:** Hidden Markov Model (HMM) ব্যবহার করে শব্দের ট্যাগ (যেমন: noun, verb) বের করা।  


## **3. Deep learning Based:(Neural Approach)**  
### **বৈশিষ্ট্য:**  
- নিউরাল নেটওয়ার্ক (RNN, Transformer) ব্যবহার করে অটোমেটিক শেখে।  
- **ফিচার ইঞ্জিনিয়ারিং** দরকার হয় না—মডেল নিজে থেকে শিখে নেয়!  
### **Era:**  
২০১০–বর্তমান (এখনকার সবচেয়ে এডভান্সড পদ্ধতি)।  
### **উদাহরণ:**  
- **ওয়ার্ড এম্বেডিং (Word2Vec, GloVe):**  
  - শব্দের ভেক্টর রিপ্রেজেন্টেশন (যেমন: "রাজা - পুরুষ + মহিলা = রানি")।  
- **সিকোয়েন্স-টু-সিকোয়েন্স (Seq2Seq):**  
  - RNN/LSTM ব্যবহার করে মেশিন ট্রান্সলেশন (যেমন: Google Neural MT, ২০১৬)।  
- **ট্রান্সফরমার মডেল (BERT, GPT):**  
  - চ্যাটজিপিটি (GPT-৩/৪), গুগলের BERT—এগুলো এখন সবচেয়ে পাওয়ারফুল।  
### **বিশেষ সুবিধা:**  
- কনটেক্স্ট বুঝতে পারে (যেমন: "বাঁশ" বলতে গাছ না বাঁশি বোঝাচ্ছে?)।  
- একই মডেল দিয়ে অনেক টাস্ক করা যায় (মাল্টি-টাস্ক লার্নিং)।  

<br>

---

---

---

<br>

# `#05 What is NLP Pipeline?`

<br>

NLP is a set of steps followed to build an end to end NLP software.

**NLP software consists of the following steps:**
- Data Acquisition: **(Gather data)**
- Text Preparation: **(Remove emoji,html tag etc.)**
    - Text Cleaning.
    - Basic text preprocessing.
    - Advance text preprocessing.
- Feature Engineering or Text Vectorization.
- Modelling
    - Model Building
    - Evaluation
- Deployment


<br>

# `#06 Text Preparation:`

<br>


![img](../img/roadmap_text.jpeg)
![img](../img/cleaning.jpeg)
![img](../img/basic_text.jpeg)
![img](../img/optional_text_01.jpeg)
![img](../img/optional_text_02.jpeg)

<br>



