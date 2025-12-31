import streamlit as st

def main():
    st.set_page_config(page_title="The Navigator Assessment", page_icon="🧭")
    
    st.title("🧭 The Navigator: The People for AI Playbook Assessment")
    st.write("Assess your organization's AI readiness by scoring the following factors.")
    st.markdown("---")

    # Define the factors, questions, and scoring guidance
    factors = [
        {
            "name": "Data Availability & Quality",
            "questions": [
                "Is there sufficient data to train an AI model effectively?",
                "Is the data clean, accurate, and consistent?",
                "Are there privacy or security concerns?"
            ],
            "guidance": "**High (4-5):** Large, clean, structured data. \n\n**Medium (2-3):** Needs cleaning/structuring. \n\n**Low (1):** Limited data or major quality issues."
        },
        {
            "name": "Measurable Outcomes",
            "questions": [
                "Can impact be measured with specific KPIs?",
                "Are there metrics to track progress?",
                "Can effectiveness be easily evaluated?"
            ],
            "guidance": "**High (4-5):** Clear, quantifiable KPIs exist. \n\n**Medium (2-3):** Hard to quantify full impact. \n\n**Low (1):** Impossible to measure objectively."
        },
        {
            "name": "Business Impact",
            "questions": [
                "Will this impact key business goals (revenue, cost, satisfaction)?",
                "Does it create new opportunities?",
                "What is the potential ROI?"
            ],
            "guidance": "**High (4-5):** High ROI and significant improvement. \n\n**Medium (2-3):** Moderate improvement to existing processes. \n\n**Low (1):** Minimal impact or negative ROI."
        },
        {
            "name": "Cost vs. Benefit",
            "questions": [
                "Do potential benefits outweigh the costs?",
                "Are there cheaper alternative solutions?"
            ],
            "guidance": "**High (4-5):** Benefits clearly outweigh costs. \n\n**Medium (2-3):** Costs and benefits are balanced. \n\n**Low (1):** High costs, limited benefits."
        },
        {
            "name": "Technical Feasibility",
            "questions": [
                "Is the technology available and integratable?",
                "Does the team have the necessary expertise?"
            ],
            "guidance": "**High (4-5):** Easy integration, expertise exists. \n\n**Medium (2-3):** Some challenges, may need external help. \n\n**Low (1):** Significant hurdles, lack of expertise."
        },
        {
            "name": "Ethical Considerations",
            "questions": [
                "Are there concerns regarding bias, privacy, or job displacement?",
                "Are policies in place for responsible use?"
            ],
            "guidance": "**High (4-5):** Minimal concerns, clear policies. \n\n**Medium (2-3):** Some concerns requiring mitigation. \n\n**Low (1):** Significant ethical risks."
        },
        {
            "name": "Employee Impact",
            "questions": [
                "Will AI augment human capabilities or replace jobs?",
                "Is there a plan for change management and reskilling?"
            ],
            "guidance": "**High (4-5):** Positive impact, growth opportunities. \n\n**Medium (2-3):** Neutral impact, some training needed. \n\n**Low (1):** Job displacement risk, heavy management required."
        }
    ]

    total_score = 0
    max_score = len(factors) * 5
    
    # Create the form
    with st.form("assessment_form"):
        for i, factor in enumerate(factors, 1):
            st.subheader(f"{i}. {factor['name']}")
            
            # Display questions
            st.write("**Key Questions:**")
            for q in factor['questions']:
                st.markdown(f"- {q}")
            
            # Display guidance in an expander to save space
            with st.expander("View Scoring Guidance"):
                st.markdown(factor['guidance'])
            
            # Slider input
            score = st.slider(f"Score for {factor['name']}", 1, 5, 3, key=factor['name'])
            total_score += score
            st.markdown("---")

        submitted = st.form_submit_button("Calculate Results")

    # Handle results
    if submitted:
        readiness_percentage = (total_score / max_score) * 100
        
        st.header("Assessment Results")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Score", f"{total_score}/{max_score}")
        with col2:
            st.metric("Readiness Rating", f"{readiness_percentage:.1f}%")
        
        # Verdict logic
        if readiness_percentage >= 80:
            st.success("Verdict: HIGH READINESS. You are well-positioned to launch your AI initiative.")
        elif readiness_percentage >= 50:
            st.warning("Verdict: MODERATE READINESS. Address the low-scoring areas before full deployment.")
        else:
            st.error("Verdict: LOW READINESS. Re-evaluate your strategy and data foundation immediately.")

if __name__ == "__main__":
    main()