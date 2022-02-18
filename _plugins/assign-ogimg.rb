Jekyll::Hooks.register :posts, :pre_render do |post|
    post.data["image"] = "/assets/ogmig/#{post.data['slug']}.jpg"
end