import streamlit as st
import requests

st.title('Support Bear', anchor=False)

tab1, tab2, tab3 = st.tabs(['Home', 'Tabs', 'Download'])

with tab1:
    st.header('Home', anchor=False)
    about_us_info = st.expander('What is Support Bear?')
    with about_us_info:
        st.write('Support Bear is an app designed to help people who need that extra support in their life.')
    help_info = st.expander('How does Support Bear help?')
    with help_info:
        st.write('Support Bear collects your data from the daily checklist and shows you which days your mood increased the most from your checked-in mood to your checked-out mood. This helps you understand what activities have the worst and best impact on your mood. Completing the daily checklist will help you feel like a much happier person. :smiley:')
    home_tab = st.expander('What is the daily checklist?')
    with home_tab:
        st.write('The daily checklist is a checklist that can be activated by clicking the "Start" button the home page. The daily checklist allows the user to complete a mood check-in, various different tasks, and a mood check-out. Completting the daily checklist earns you rewards. Your data from the checklist is saved in the "Report" tab, and you will recieve weekly reports which shows you which days you had the biggest increase in your overall mood.')

with tab2:
    st.header('Tabs', anchor=False)
    journal_tab = st.expander('What is the journal tab?')
    with journal_tab:
        st.write('The journal tab allows you to write in and save any of the three journals: Basic Journal, Mood Journal, Vent Journal')
    activities_tab = st.expander('What is the activities tab?')
    with activities_tab:
        st.write('The activities tab contains of a pre-made list of popular activities that you can do. You can also add your own.')
    exercise_tab = st.expander('What is the exercise tab?')
    with exercise_tab:
        st.write('The exercise tab contains three different workouts for different difficulty levels: Beginner, Intermediate, Advanced')
    diet_tab = st.expander('What is the diet tab?')
    with diet_tab:
        st.write('The diet tab has a list of popular diets with the purpose of each diet and an example meal.')
    tips_tab = st.expander('What is the tips tab?')
    with tips_tab:
        st.write('The tips tab has a variety of different tips for common issues many people face, such as low self-esteem')
    goals_tab = st.expander('What is the goals tab?')
    with goals_tab:
        st.write('The goals tab allows you to write down any long-term or short-term goals you have.')
    reward_tab = st.expander('What is the rewards tab?')
    with reward_tab:
        st.write('The rewards tab keeps track of all the different rewards you have earned through completing the daily checklist certain amount of times.')
    report_tab = st.expander('What is the report tab?')
    with report_tab:
        st.write('The report tab keeps track of all your daily checklist entries, and weekly reports will be created to show you which days you experienced your best and worst mood change. Days where you have your most positive mood change will be highlighted pink.')

def download_release_asset(owner, repo, tag, asset_name, output_path):
    # GitHub API URL for the releases
    api_url = f"https://api.github.com/repos/{owner}/{repo}/releases/tags/{tag}"
    
    # Send a request to the GitHub API
    response = requests.get(api_url)
    response.raise_for_status()
    
    # Parse the JSON response to find the asset
    release_info = response.json()
    assets = release_info.get('assets', [])
    
    # Find the asset URL by name
    asset_url = None
    for asset in assets:
        if asset['name'] == asset_name:
            asset_url = asset['browser_download_url']
            break
    
    if not asset_url:
        raise ValueError(f"Asset '{asset_name}' not found in release '{tag}'")
    
    # Download the asset
    download_response = requests.get(asset_url, stream=True)
    download_response.raise_for_status()
    
    # Write the asset to a file
    with open(output_path, 'wb') as f:
        for chunk in download_response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"Downloaded {asset_name} to {output_path}")

# Example usage
owner = 'TEPCoder24'
repo = 'Support-Bear-App'
tag = 'v1'
asset_name = 'Support.Bear.exe'
output_path = 'Support.Bear.exe'

download_release_asset(owner, repo, tag, asset_name, output_path)

def downloaded():
    st.balloons()
    with open('Download_number.txt', 'a') as file:
        file.write('\n')
        file.close()

with tab3:
    with open('Support.Bear.exe', 'rb') as download_file, open('Download_number.txt', 'r') as number_file:
        num_lines = number_file.readlines()
        num = len(num_lines)
        st.header('Download', anchor=False)
        st.subheader('Download for Windows', divider='red', anchor=False)
        download_windows = st.download_button('Download for Windows', data=download_file, file_name='Support Bear.exe', on_click=downloaded)
        st.write(f'Total downloads: {num}')
