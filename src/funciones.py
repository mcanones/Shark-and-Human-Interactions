import re
import matplotlib.pyplot as plt

############################################################ CLEANING FUNCTIONS ####################
####################################################################################################

def clean_date(s):
    search=re.search(r"(Jan)|(Feb)|(Mar)|(Apr)|(May)|(Jun)|(Jul)|(Aug)|(Sep)|(Oct)|(Nov)|(Dec)", s)
    if search != None:
        return search.group()
    else:
        return None


def clean_time(s):
    search=re.search(r"(\d{2}h)|(morning)|(afternoon)|(noon)|(night)|(dawn)|(evening)|(am)|(a.m)|(pm)|(p.m)", str(s).lower())
    if search != None:
        return search.group()
    else:
        return None
    
def clean_activity(s):
    search=re.search(r"(surfing)|(swimming)|(fishing)|(bathing)|(wading)|(diving)|(scuba diving)|(standing)|(windsurfing)|(free diving)|(pearl diving)|(kayaking)|(body surfing)|(snorkeling)|(body boarding)|(fell)|(body surfing)|(floating)|(boogie boarding)|(rowing)|(surf skiing)|(yachting)|(walking)|(canoeing)|(treading water)|(shark fishing)", str(s).lower())
    if search != None:
        return search.group()
    else:
        return None

   ####################################################################################################
####################################################################################################


############################################################ ANALYSIS FUNCTIONS ####################
####################################################################################################

def plot_graph_mat(sub_df, names, colors, title, rows, cols, typeplot, fsize=(20, 10), xaxes="Country", yaxes="counts"):
    fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=fsize)
    fig.tight_layout(pad=0.4, w_pad=0.5, h_pad=13.0)
    fig.text(-0.04, 0.5, title, va='center', rotation='vertical',fontsize=24)
    count=0
    for i1 in range(rows):
        for i2 in range(cols):
            df_aux = sub_df[[xaxes,yaxes]][sub_df[typeplot]==names[count]].sort_values(by=[yaxes], ascending=False).head(10)
            df_aux.plot.bar(ax=axes[i1,i2],x=xaxes, y=yaxes, rot=90, label=names[count], color=colors[count]).xaxis.set_label_text("")
            count+=1
    fig.savefig('output/graph'+typeplot, bbox_inches='tight')
   
    
def plot_graph_lin(sub_df, names, colors, title, rows, cols, typeplot, fsize=(20, 10), xaxes="Country", yaxes="counts"):
    fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=fsize)
    fig.tight_layout(pad=0.4, w_pad=0.5, h_pad=13.0)
    fig.text(-0.04, 0.5, title, va='center', rotation='vertical',fontsize=24)
    count=0
    for i2 in range(cols):
        df_aux = sub_df[[xaxes,yaxes]][sub_df[typeplot]==names[count]].sort_values(by=[yaxes], ascending=False).head(10)
        df_aux.plot.bar(ax=axes[i2],x=xaxes, y=yaxes, rot=90, label=names[count], color=colors[count]).xaxis.set_label_text("")
        count+=1
    fig.savefig('output/graph'+xaxes, bbox_inches='tight')
    
####################################################################################################
####################################################################################################

   