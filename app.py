import streamlit as st
import numpy as np

from components.maps import *
from components.wordclouds import *
from components.ngrams import *
# from components.readability import *

# Similarity file commented out because as it downloads a 1.6gb model everytime ir runs
# from components.similarity import *

companies = ("Dunzo", "Facebook", "Instagram",
             "Paypal", "Playstore", "Twitter", "Uber")

# Call functions ased on map value
mapFunc = {
    "GDPR Compliant Countries": gdpr_compliant_map,
    "Facebook": fb_active_map,
    "Twitter": twitter_active_map,
    "Instagram": insta_active,
    "Paypal": paypal_active,
    "Uber": uber_active
}

# BODY STARTS HERE

# SIDEBAR
nav = st.sidebar.selectbox("Navigation", ["Overview", "Wordclouds and Maps", "Pilot Readability Scores", "Similarity Scores"])

if nav == "Overview":

    st.header("Privacy Policy Analysis: What does it say?")
    st.subheader("DIRI-ISB Hyderabad")
    st.markdown("")

    st.markdown("### In our work, we tried to understand the nature of Privacy Privacy policy documents using metrics \
            defined by computational linguistic methods.")

    st.markdown("#### Primarily, we tried to work on the following three points:")
    st.markdown("**The _essence_ of the policy:** What are the most common words and phrases in the policy? At first glance what information does it convey?")
    st.markdown("**Geographical variation:** Are same rules applicable to every person on the planet Earth? Or different ones for a person from The US and a person from China?")
    st.markdown("**Readability Scores:** How readable a policy is? Can a middle schol student understand it? Or does it need a Masters student to figure out what it says?")
    st.markdown("**Similarity Scores:** Do the policies follow a common flow of thought? Are there duplicate policies throughout companies? Or are they contrasting in what they convey?")

    
    st.markdown("---")

    st.subheader("How to Use?")
    st.markdown("Use the sidebar on the left to navigate to the following sections as desired:")
    st.markdown("- **Wordclouds and Maps:** To get the _essence_ of the policies and the geographical variations")
    st.markdown("- **Pilot Readability Scores:** To get an idea about how readable a certain privacy policy is")
    st.markdown("- **Similarity Scores:** How similar privacy policies are across different companies")

    # READIBILITY SCORES END


elif nav == "Wordclouds and Maps":

    st.header("The _essence_ of a privacy policy")

    st.write("We attempted to have a look at what is the essence of the documents. We \
            analysed word clouds to gain a sense of what the main focus points of\
            each policy document are and n-grams (uni-, bi-, tri-, 4grams) for\
            each of the privacy policy texts. These have been displayed to provide\
            an overview for the user.")
    # WORDCLOUDS start
    st.subheader("Wordclouds")

    wc_col_1, wc_col_2 = st.beta_columns(2)

    val = wc_col_1.selectbox(
        'Company name: ',
        companies
    )
    gram = wc_col_2.selectbox(
        'Gram: ',
        (1, 2, 3, 4)
    )

    wc_content_col_1, wc_content_col_2 = st.beta_columns((5,4))

    wc_content_col_1.image(images[val][gram-1], use_column_width=True)
    # WORDCLOUDS end

    wc_content_col_2.write(csvs[val][gram-1], use_column_width=True)
    # TFIDF end

    st.markdown("---")
    st.header("Geographical Variation")
    st.header("Were the policies defined differently for different geographical regions?")

    st.write("GDPR being the most strictly defined data privacy laws, formed the basis\
            of our comparative assessment. We start out by having a look at countries \
            which lie within the purview of this law and proceed to find out whether or\
            not data based apps and services choose to define their policies differently in\
            regions not governed by these laws. We found that some companies operated using \
            the same policies globally, some decided to follow different privacy policies in\
            different regions, as well as some companies that, due to data privacy concerns of\
            current governing regimes, were non operational in certain countries. To have a \
            look at how things are at the global level, we displayed this data in the form\
            of color coded maps of the world for ease of comprehension.")


    #st.title("Privacy Visualisations")

    # MAPS start
    st.subheader("Maps")

    mapOpt = st.selectbox(
        'Select option: ',
        ("GDPR Compliant Countries", "Facebook", "Twitter", "Instagram", "Paypal", "Uber")
    )

    if mapOpt != "GDPR Compliant Countries":
        st.write("Privacy policy is consistent in like colored regions")
    mapFunc[mapOpt]()
    # MAPS end


if nav == "Pilot Readability Scores":
    st.header("Were the policies written in a manner that made them easy to comprehend?")

    st.write("To answer this question using metrics instead of intuition, we relied on two \
            scores that would measure the reading comprehension or difficulty of the text, \
            viz, the Flesch’s Reading Ease score and the Dale Chall Readability score. The \
            former uses the length of words and sentences to factor the difficulty level in \
            reading while the latter relies on a list of 3000 easy to understand words, \
            categorizing any other non commonly occurring word as hard. Scores on the Flesch’s\
            scale lie within the range of 0-100, with higher scores indicating more readable texts. \
            Similarly, on the Dale Chall reading scores, scores around 4.9 or lower indicate text \
            that could be comprehended below grade 4 reading comprehension levels, whereas scores \
            higher than 10 would require a reading level of a college graduate.")

    # READIBILITY SCORES
    st.subheader("Readability Scores")

    # Data stored as CSV to make the app faster

    # convert to CSV
    # df = ReadabilityScores()
    # csv = df.to_csv('./assets/readability.csv')
    # st.write(df)

    csv_readability = pd.read_csv('./assets/readability.csv')
    st.write(csv_readability)

if nav == "Similarity Scores":

    st.header("Were the policies worded similarly?")
    st.write("To answer this question, we relied on\
            using sentence embeddings in the form of unweighted averages and \
            smooth inverse frequencies. Using a scaled similarity score we\
            calculate the pairwise similarity scores for a small set of policies, \
            displayed as a matrix. Positive scores indicated similarity between the\
            documents, and negative scores, dissimilarity on the basis of\
            their representations in a vector space.")


    # SMILARITY SCORES START
    st.subheader("Similarity Scores")
    csv_similarity = pd.read_csv('./assets/similarity.csv')
    df_similarity = pd.DataFrame(csv_similarity)

    df_similarity = df_similarity.set_index('Company')

    st.table(df_similarity)
    # SIMILARITY SCORES END


