json.extract! book, :id, :name, :code_num, :created_at, :updated_at
json.url book_url(book, format: :json)
