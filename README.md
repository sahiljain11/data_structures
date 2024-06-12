
## Please add two units for each

First, checkout a new branch:
```bash
git checkout -b <github_username>/<data_structure_name>_tests
```
Example:
```bash
git checkout -b sahiljain11/arraylist_tests
```

Then, add your new code and do the following with a commit message:
```bash
git commit -m "<insert a meaningful commit message>"
```

Then, push your changes to Github:
```bash
git push -u origin <github_username>/<data_structure_name>_tests
```
You only need to do this above command once per data structure. You can simply do `git push` if you have more commits to push to Github.

Then, you'll need to make a Pull Request. Once that pull request has been approved by me, you can merge your changes in by hitting the button and deleting this branch:
```bash
git checkout main
git branch -D <github_username>/<data_structure_name>_tests
```