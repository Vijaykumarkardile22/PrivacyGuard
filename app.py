
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="PrivacyGuard",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ PrivacyGuard")
st.subheader("Personal Data Privacy Dashboard")

st.write(
    "Understand the permissions you select for applications "
    "and review potential privacy risks."
)

st.info(
    "Educational prototype: assessments use your inputs. "
    "This app does not scan your device or verify actual app behavior."
)

st.header("1. Application Details")

app_name = st.text_input(
    "Application name",
    placeholder="Example: Instagram"
)

st.write("Select the permissions you want to assess:")

location = st.checkbox("Location access")
contacts = st.checkbox("Contacts access")
photos = st.checkbox("Photos and media access")
camera = st.checkbox("Camera access")
microphone = st.checkbox("Microphone access")

permissions = {
    "Location": location,
    "Contacts": contacts,
    "Photos and media": photos,
    "Camera": camera,
    "Microphone": microphone
}

selected = [
    permission
    for permission, enabled in permissions.items()
    if enabled
]

# Demonstration score only; not a validated security measurement.
risk_score = min(len(selected) * 20, 100)

if risk_score >= 60:
    risk_level = "High"
elif risk_score >= 20:
    risk_level = "Moderate"
else:
    risk_level = "Low"

st.header("2. Privacy Assessment")

col1, col2, col3 = st.columns(3)

col1.metric("Selected permissions", len(selected))
col2.metric("Illustrative risk score", f"{risk_score}/100")
col3.metric("Risk category", risk_level)

if st.button("Assess Privacy", type="primary"):
    if not app_name.strip():
        st.warning("Please enter an application name.")
    else:
        st.success(f"Assessment completed for {app_name.strip()}.")

        if selected:
            st.write("Selected permissions:")
            for permission in selected:
                st.write(f"- {permission}")
        else:
            st.write("No permissions were selected.")

        st.subheader("Privacy Recommendations")

        if location:
            st.write(
                "- Review whether location access is needed "
                "all the time or only while using the app."
            )

        if contacts:
            st.write(
                "- Check whether contact access is necessary "
                "for the app's main features."
            )

        if photos:
            st.write(
                "- Prefer selecting only specific photos "
                "when that option is available."
            )

        if camera:
            st.write(
                "- Allow camera access only when required."
            )

        if microphone:
            st.write(
                "- Review microphone access and disable it "
                "when it is not needed."
            )

        if not selected:
            st.write(
                "- Review the app's privacy policy and "
                "check its permissions periodically."
            )

        st.caption(
            "A selected permission does not prove misuse. "
            "Review the app's purpose and actual settings."
        )

st.header("3. Permission Overview")

chart_data = pd.DataFrame({
    "Permission": list(permissions.keys()),
    "Selected": [
        1 if enabled else 0
        for enabled in permissions.values()
    ]
})

fig = px.bar(
    chart_data,
    x="Permission",
    y="Selected",
    title="Selected Application Permissions",
    range_y=[0, 1.2]
)

st.plotly_chart(fig, use_container_width=True)
