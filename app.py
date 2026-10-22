from flask import Flask, render_template, request, redirect

from database import add_asset, create_database, get_asset_count, get_assets, delete_asset, get_asset_by_id, update_asset

app = Flask(__name__)

create_database()

@app.route("/")
def home():
    assets = get_assets()
    count = get_asset_count()
    return render_template("home.html", assets=assets, count=count)

@app.route("/assets")
def assets():
    assets = get_assets()
    return render_template("assets.html", assets=assets)


@app.route("/reports")
def reports():
    return render_template("device_reports.html")

@app.route("/add_asset", methods=["GET", "POST"])
def add_asset_route():
    if request.method == "POST":
        add_asset(
            name=request.form["name"],
            type=request.form["type"],
            user=request.form["user"],
            department=request.form["department"],
            serial_number=request.form["serial_number"],
            status=request.form["status"]
        )

        return redirect("/assets")
    return render_template("add_asset.html")

@app.route("/delete_asset/<int:asset_id>")
def delete_asset_route(asset_id):
    delete_asset(asset_id)
    return redirect("/assets")

@app.route("/update_asset/<int:asset_id>", methods=["GET", "POST"])
def update_asset_route(asset_id):
    if request.method == "POST":
        update_asset(
            asset_id=asset_id,
            name=request.form["name"],
            type=request.form["type"],
            user=request.form["user"],
            department=request.form["department"],
            serial_number=request.form["serial_number"],
            status=request.form["status"]
        )
        return redirect("/assets")
    asset = get_asset_by_id(asset_id)
    return render_template("update_asset.html", asset=asset)


if __name__ == '__main__':
    app.run(debug=True)


#Add search function within home page 
#Start turning type into dropdowns - server, pc, laptop, etc