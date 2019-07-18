class RenameCodeNumColumnToBook < ActiveRecord::Migration[5.2]
  def change
      rename_column :books, :code_num, :code_id
  end
end
