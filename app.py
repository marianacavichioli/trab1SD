from flask import Flask
from flask_restful import Api, Resource, reqparse
import linda

app = Flask(__name__)
api = Api(app)
linda.connect()

blog = linda.TupleSpace()
linda.universe._out(("Blog", blog))
#blog = linda.universe._rd(("Blog",linda.TupleSpace))

class Blog(Resource):
    def get(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("topic")
        args = parser.parse_args()
        post = blog._rd((name, args["topic"], str))
        posts = post.splitlines()
        return posts

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("topic")
        parser.add_argument("post")
        args = parser.parse_args()

        message = blog._out((name, args["topic"], args["post"]))
        return message, 201

    def delete(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("topic")
        parser.add_argument("post")
        args = parser.parse_args()
        
        message = blog._in((name, args["topic"], args["post"]))
        return message, 200
      
api.add_resource(Blog, "/blog/<string:name>")

app.run(debug=True)