Jekyll::Hooks.register :posts, :pre_render do |post|
    post.data["image"] = "/assets/ogimg/#{post.data['slug']}.jpg"
end