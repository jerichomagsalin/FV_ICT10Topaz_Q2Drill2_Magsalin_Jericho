from pyscript import display, document

# current scores for lists

club_members = {"Jericho Magsalin"}

def add_member (e):
    global club_members
    club_members = club_members.union("data")
    display("data", target = "newmember")

    document.getElementById("firstname").value
    document.getElementById("lastname").value