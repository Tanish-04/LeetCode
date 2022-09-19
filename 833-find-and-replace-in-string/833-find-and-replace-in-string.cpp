class Solution {
public:
    string findReplaceString(string s, vector<int>& indices, vector<string>& sources, vector<string>& targets) {
        string res = s;
        map<int, pair<string, string>> map;
        
        for(int i=0; i<indices.size(); i++){
            map[indices[i]] = {sources[i], targets[i]};
        }
        
        int dx = 0;
        
        for(auto [idx, pair]: map){
            if(s.substr(idx, pair.first.size()) == pair.first){
                res.erase(idx + dx, pair.first.size());
                res.insert(idx + dx, pair.second);
                dx += (pair.second.size() - pair.first.size());
            }
        }
        return res;
    }
};