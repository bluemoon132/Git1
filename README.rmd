# Các câu lệnh command line trong Git
- Thiết lập chứng thực cá nhân
	+ *git config --global user.name "Tên người dùng"* để khai báo tên người dùng
	+ *git config --global user.email "Địa chỉ email"* để khai báo địa chỉ mail
	+ *cat ~/.gitconfig* để xem lại chứng thực cá nhân trên user
- Tạo một REPOSITORY
	+ Tạo local repository (Kho sẽ lưu trên máy tính cá nhân)
		- Truy cậo vào thư mục mã nguồn gốc với lệnh *cd*
		- Sử dụng lệnh *git init tên folder* để khởi tạo repository trong thư mục đó
		- Nếu có sẵn mã nguồn, dùng lệnh *git add tên_file* hoặc *git add ** để add toàn bộ các file
		- Sử sụng *git status* để xem các file đã đc track
		- Sự dụng *git commit -m "Lời nhắn"* để tiến hành uỷ thác nhằm lưu lại các file đã add hoặc lưu lại những file thay đổi
	+ Tạo repository trên Github
		- Sau khi tạo xong, kho chứ trên Github sẽ có địa chỉ **https://github.com/$user-name/$repository**
		- Clone lại kho chứa về máy tính bằng lệnh *git clone địa_chỉ*
		- Sử dụng lệnh *git push origin master* để đẩy lên Github
- COMMIT và STAGGING AREA
	+ Điều kiện để commit 1 file:
		- File phải đc track có thế track bằng *git add tên_file*
- GIT LOG và UNDO COMMIT
	+ Dùng *git log* để xem lịch sử các lần commit trước hoặc thêm *git log -p* để hiện thêm các chi tiết
	+ Dùng *git commit --amend -m "Tên_file"* để undo commit
	+ Loại bỏ file khỏi Staging Area bằng lệnh *git reset HEAD tên_file*
	+ Loại bỏ file khỏi Staging Area bằng lệnh *git reset HEAD tên_file*