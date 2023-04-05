# Twitter Author ID Finder + Follower Count for Epicosm

This code is for use alongside the Epicosm Twitter harvesting software. This code should be used when you have a list of usernames of participants but not author_ids. The Epicosm code used to harvest Tweets of ALSPAC participants currently creates datasets which have the participant's Twitter author_id, but not their usernames. This code uses the user_list.txt file containing the list of ALSPAC participant user_names, and finds the author_id of these users. This means the the Epicosm generated dataset can be linked to the user list, for prepartation for use of researchers. The code also harvests the current number of followers that each participant has, which the Epicosm program current does not do.

## Instructions

1). You must have an existing Epicosm directory and user_list.txt file. Each username must be on a seperate line and must link to an existing and non-private account. If the account is not existing or is private, the software will not work. 

2). In the Epicosm directory run this code to extract this software. 

```python
git clone https://github.com/JoinsonCoding/Epicosm_Twitter_ID_Finder.git 
```

This will generate a folder called Epicosm_Twitter_ID_Finder

3). Use the following code to enter the new folder

```python
cd Epicosm_Twitter_ID_Finder
```

Create a new user_list.txt file and copy the contents of the existing one into this new folder. 

4). Installing requirements

This code uses the pandas and Tweepy packages, which may need to be installed, using the following code. 

```python
pip install pandas
```

```python
pip install Tweepy
```

5). Use the following code to run the software

```python
python ID_finder.py
```

if this doesn't work, it may be neccessary to use this code instead

```python
python3 ID_finder.py
```

This will generate a csv file in the directory you're currently in, with columns for the username, author_id and current number of followers. 
