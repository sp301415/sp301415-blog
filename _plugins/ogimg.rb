# Generate Opengraph Image using generate-ogimg.py
system("pip install pillow")
system("python _plugins/generate-ogimg.py")

Jekyll::Hooks.register :posts, :pre_render do |post|
    post.data["image"] = "/assets/ogimg/#{post.data['slug']}.jpg"
end