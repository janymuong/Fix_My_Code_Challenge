class Post < ApplicationRecord
  has_many  :comments, dependent: :destroy
  has_boolean :online, default: true
  validates :title, presence: true, length: {minimum: 5}
	validates :body,  presence: true
end
