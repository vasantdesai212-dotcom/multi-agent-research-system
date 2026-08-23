import streamlit as st
from pipeline import run_research_pipeline


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main page */
    .main {
        padding-top: 2rem;
    }

    /* Header */
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        font-size: 1.1rem;
        opacity: 0.7;
        margin-bottom: 2rem;
    }

    /* Agent cards */
    .agent-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        margin-bottom: 1rem;
        background: rgba(128, 128, 128, 0.05);
    }

    .agent-title {
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }

    .agent-description {
        font-size: 0.9rem;
        opacity: 0.7;
    }

    /* Report box */
    .report-container {
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        background: rgba(128, 128, 128, 0.03);
    }

    /* Footer */
    .footer {
        text-align: center;
        opacity: 0.5;
        margin-top: 3rem;
        font-size: 0.85rem;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🔬 Research System")

    st.markdown(
        """
        Your research pipeline uses multiple AI components
        to search, read, write, and critique information.
        """
    )

    st.divider()

    st.markdown("### 🤖 Agent Pipeline")

    st.markdown(
        """
        <div class="agent-card">
            <div class="agent-title">🔎 Search Agent</div>
            <div class="agent-description">
                Finds recent and reliable information.
            </div>
        </div>

        <div class="agent-card">
            <div class="agent-title">📖 Reader Agent</div>
            <div class="agent-description">
                Scrapes and analyzes relevant sources.
            </div>
        </div>

        <div class="agent-card">
            <div class="agent-title">✍️ Writer Chain</div>
            <div class="agent-description">
                Creates the research report.
            </div>
        </div>

        <div class="agent-card">
            <div class="agent-title">🧐 Critic Chain</div>
            <div class="agent-description">
                Reviews and evaluates the final report.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.caption("Powered by your existing multi-agent backend")


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🔬 Multi-Agent Research System</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
    "Give the agents a topic and let them research, analyze, write, and critique it."
    "</div>",
    unsafe_allow_html=True,
)


# ============================================================
# TOPIC INPUT
# ============================================================

st.markdown("### 🎯 Research Topic")

topic = st.text_input(
    "Enter a topic",
    placeholder="Example: The impact of AI agents on modern businesses",
    label_visibility="collapsed",
)


# ============================================================
# RUN BUTTON
# ============================================================

run_button = st.button(
    "🚀 Start Research",
    type="primary",
    use_container_width=True,
)


# ============================================================
# PIPELINE EXECUTION
# ============================================================

if run_button:

    # --------------------------------------------------------
    # Validate input
    # --------------------------------------------------------

    if not topic.strip():
        st.warning("Please enter a research topic first.")

    else:

        # ----------------------------------------------------
        # Progress UI
        # ----------------------------------------------------

        st.markdown("## ⚙️ Research Pipeline")

        progress = st.progress(0)

        status = st.empty()

        try:

            # ------------------------------------------------
            # Step 1
            # ------------------------------------------------

            status.info("🔎 Step 1/4 — Search Agent is researching...")
            progress.progress(10)

            # ------------------------------------------------
            # Run your EXISTING backend
            # ------------------------------------------------

            state = run_research_pipeline(topic.strip())

            # ------------------------------------------------
            # Pipeline completed
            # ------------------------------------------------

            progress.progress(100)
            status.success("✅ Research pipeline completed successfully!")

            st.divider()

            # =================================================
            # RESULTS
            # =================================================

            st.markdown("## 📊 Research Results")

            # ------------------------------------------------
            # Search Results
            # ------------------------------------------------

            with st.expander(
                "🔎 Search Results",
                expanded=False,
            ):

                search_results = state.get("search_results", "")

                if search_results:
                    st.markdown(search_results)
                else:
                    st.info("No search results were returned.")

            # ------------------------------------------------
            # Scraped Content
            # ------------------------------------------------

            with st.expander(
                "📖 Scraped Source Content",
                expanded=False,
            ):

                scraped_content = state.get(
                    "scraped_content",
                    "",
                )

                if scraped_content:
                    st.markdown(scraped_content)
                else:
                    st.info("No scraped content was returned.")

            # ------------------------------------------------
            # Final Report
            # ------------------------------------------------

            st.markdown("## 📝 Final Research Report")

            report = state.get(
                "report",
                "",
            )

            if report:

                st.markdown(
                    '<div class="report-container">',
                    unsafe_allow_html=True,
                )

                st.markdown(report)

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True,
                )

            else:

                st.warning(
                    "The writer chain did not return a report."
                )

            # ------------------------------------------------
            # Critic Feedback
            # ------------------------------------------------

            st.markdown("## 🧐 Critic Review")

            feedback = state.get(
                "feedback",
                "",
            )

            if feedback:

                st.markdown(
                    '<div class="report-container">',
                    unsafe_allow_html=True,
                )

                st.markdown(feedback)

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True,
                )

            else:

                st.warning(
                    "The critic chain did not return feedback."
                )

            # ------------------------------------------------
            # Download Report
            # ------------------------------------------------

            if report:

                st.markdown("## 📥 Export")

                st.download_button(
                    label="Download Research Report",
                    data=report,
                    file_name="research_report.md",
                    mime="text/markdown",
                    use_container_width=True,
                )

        except Exception as e:

            progress.empty()
            status.empty()

            st.error(
                "❌ Something went wrong while running the research pipeline."
            )

            with st.expander("Show technical error"):

                st.exception(e)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        Multi-Agent Research System • Search → Read → Write → Critique
    </div>
    """,
    unsafe_allow_html=True,
)
