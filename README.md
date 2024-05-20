This script retrieves all Layer3 quests (except infinity) that allow minting a cube via an API request. The quest names "slugs" are saved in a text file. The program then checks if the latest slugs returned by the API are present in the file. If not, a notification will be sent to a webhook (Discord) with the name and link to the quest.

You can run this script on any server that can use Python.
