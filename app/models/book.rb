class Book < ApplicationRecord
  scope :sort_by_code_id, -> (count) { order(code_id: :desc).limit(count) }
end
