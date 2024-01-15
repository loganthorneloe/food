# Food By Logan

Here is a **very** naive method of automating dinner planning. It's super simple, requires nothing in the cloud, and can be run on your phone.

A Shortcut on my iPhone runs the Python script in this repo on my Mac. That prints the meals and shopping list which is received by the shortcut, separated, and pushed into a 'Meals w/Prep' and 'Shopping List' in the Reminders app set up with alerts on the Reminders.

This works on a food.yaml that has all the protein, carbs, and vegs in it to plan simple meals that consist of one of each. I have mine set up for one night to be chicken nuggets and mac and cheese, one night to be Costco pizza, and one night to be an audible/leftovers (otherwise we don't end up using our leftovers). It also forces one night to be chicken breast and pasta with a protein. It then plans three more meals without duplicating protein, carb, or veg. This keeps meals and shopping simple but healthy and consistent.

I also set it up to create Reminders for the night before on meals where I may need to meal prep (such as marinating chicken).

## Things to change to use this repo yourself

* food.yaml - set it up with your preferred foods
* shortcut path - change the 'Run Shell via SSH' shortcut action to point to where you've cloned this repo
* shortcut reminders list - change the Reminders lists the meals/shopping list is saved to to match what you need

If you're running this without a Mac/iPhone all the logic is in the python script. You'll just need a way to run it and a place to store reminders/your shopping list accessible via API.