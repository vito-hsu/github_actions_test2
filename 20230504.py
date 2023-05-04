# In this tutorial, I'll demo how to use GitHub Actions.
# With GitHub Actions, there are several demos for many programming use cases, and I'll use the demo for python app.
# In the right hand side, it's our final results.
# Ok~ Let's biuld it.
# 1. Search python in Actions. Here, we click Python application and start commit.
# 2. If you do this step, you can click here and see it.
# 3. Because we don't give the test script .py.
# 4. Let's revise it. And try again. It's building...and successful.
# 5. Let's try pull/push files to the repository.
# 6. This step, we can revise the .yml file, core file for actions, from ~
# 7. Because I hope to test the .py file, we should revise the .yml again.
# 8. PUSH

# Step1. PULL files from GitHub
#   git init
#   git remote add origin https://github.com/vito-hsu/github_actions_test2.git
#   git pull origin main

# Step2. PUSH (updated) files to GitHub
#   git add .
#   git commit -m 'first version'
#   git push origin main


def test_1():
    a = 1 
    b = 2 
    assert b > a


def test_2():
    a = 2 + 2
    b = 4 + 4
    assert a < b


# def test_3():
#     a = 2 + 2
#     b = 4 + 4
#     assert a == b