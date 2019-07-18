class Book < ApplicationRecord
  scope :sort_by_code_id, -> { order(id: :desc).limit(100) }
end
