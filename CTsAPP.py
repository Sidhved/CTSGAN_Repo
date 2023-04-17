from hydralit import HydraApp
import streamlit as st
import apps

st.set_page_config(page_title='CTsGAN',page_icon="🐙",layout='wide',initial_sidebar_state='auto',)

if __name__ == '__main__':
    over_theme = {'txc_inactive': '#FFFFFF'}
    app = HydraApp(
        title='CTsGAN',
        hide_streamlit_markers=True,
        use_navbar=True, 
        navbar_sticky=False,
        navbar_animation=True,
        navbar_theme=over_theme,
    )

app.add_app("Home", icon="🏠", app=apps.HomeApp(title='Home'),is_home=True)
app.add_app("Source Code", icon="fab fa-github", app=apps.goGitHub(title="Source Code"))
app.add_app("References", icon="🔎", app=apps.References(title='References'))


app.run()