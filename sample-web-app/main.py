from flask import Flask, render_template, request
server = Flask(__name__)


@server.route('/mydetail', methods=['GET', 'POST'])
def show_my_details():

    if request.method == 'POST':
        form_data = request.form
        print("Form data: ", form_data)
        name = form_data['name']
        email = form_data['email']
        print("Name: ", name)
        print("Email: ", email)
        return render_template("my/show.html", name=name, email=email)

    return render_template("my/detail.html")


server.run(debug=True)
