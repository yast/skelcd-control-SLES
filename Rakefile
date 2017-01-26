require "yast/rake"

Yast::Tasks.configuration do |conf|
  # lets ignore license check for now
  conf.skip_license_check << /.*/
end

# check also the syntax of the XML files
task :"check:syntax" do
  sh "make -C control check"
end
