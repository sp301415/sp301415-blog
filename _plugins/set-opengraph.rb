system("python _plugins/generate-opengraph.py")

Jekyll::Hooks.register :posts, :pre_render do |post|
    post.data["image"] = "/assets/opengraph/#{post.data['slug']}.png"
end